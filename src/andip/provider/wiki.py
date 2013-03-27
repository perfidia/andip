# -*- coding: utf-8 -*-
'''
Created on Apr 27, 2012

@author: Bartosz Alchimowicz
'''

import urllib
import re
import copy

from andip import DataProvider
from andip.database import database
from andip.wiki import schema

class WikiProvider(DataProvider):
    def __init__(self, url):
        self.__url = url
        
    def _get_word(self, conf):
        assert isinstance(conf, tuple)
        assert len(conf) == 3
        assert isinstance(conf[0], basestring)
        assert isinstance(conf[1], basestring)
        assert isinstance(conf[2], dict)
        #

    def _get_conf(self, word):
        assert isinstance(word, str)
        
        return urllib.urlopen(self.__url + 'w/api.php?format=xml&action=query&prop=revisions&rvprop=content&titles=' + word).read()
        
    def _get_dump(self, word=None, conf=None):
        """
        Dump data of a specified word in a string recognazible by FileProvider.
        @param word: a word to dump
        @param conf: restric dump to a specified configuration
        @return: string in a JSON format
        """
        pass

    
class PlWikiProvider(WikiProvider):
    
    def __init__(self, url):
        WikiProvider.__init__(self, "http://pl.wiktionary.org/")
        self.__schema_adjective = None
        self.database = database.Database(url)
    
    def close_database(self):
        self.database.close()
    
    def _load(self, data_set):
        return eval(open(data_set + ".txt").read())
    
    def __get_conf_noun(self, base_word, data):
        configuration = {}
        configuration[base_word] = {}
        configuration[base_word]['przypadek'] = {}
        
        for przypadek in ['mianownik', 'dopełniacz', 'celownik', 'biernik', 'narzędnik', 'miejscownik', 'wołacz']:
            configuration[base_word]['przypadek'][przypadek] = {}
            configuration[base_word]['przypadek'][przypadek]['liczba'] = {}
            #for liczba in ['pojedyncza', 'mnoga']:
            #    config[base_word]['przypadek'][przypadek][liczba] = ""

        for conf in data:
            config = dict()
            conf = conf.replace("|", "").split("\n")
            for element in filter(None, conf):
                tmp = element.split("=")
                przypadek = tmp[0].lower().split(' ')[0]
                liczba = tmp[0].lower().split(' ')[1]
                tmp[1] = tmp[1].replace(" ", "")
                if liczba == 'lp':
                    liczba = "pojedyncza"
                else:
                    liczba = "mnoga"
                configuration[base_word]['przypadek'][przypadek]['liczba'][liczba] = tmp[1]
            self.database.save_noun(configuration[base_word], base_word)  
            return configuration[base_word]

    def __get_word_noun(self, data, case, number):
        
        return data['przypadek'][case]['liczba'][number]
    
    def __get_conf_verb(self, base_word, data):
        if len(data) == 0:
            raise Exception("verb error")
        
        conf = data[0]
        config = dict()
        conf = conf.replace("| ", "").split("\n")
        for element in filter(None, conf):  # filter removes empty elements
            tmp = element.split("=")
            config[tmp[0]] = tmp[1]
        
        if config['dokonany'] == 'tak':
            done = 'dokonane' 
        else:
            done = 'niedokonane'
        
        configuration = {}
        configuration[base_word] = {}
        configuration[base_word]['aspekt'] = {}
        configuration[base_word]['aspekt'][done] = {}
        configuration[base_word]['aspekt'][done]['forma'] = {}
        for forma in ['czas terazniejszy', 'czas przeszly']:
            configuration[base_word]['aspekt'][done]['forma'][forma] = {}
            configuration[base_word]['aspekt'][done]['forma'][forma]['liczba'] = {}
            for liczba in ['pojedyncza', 'mnoga']:
                configuration[base_word]['aspekt'][done]['forma'][forma]['liczba'][liczba] = {}
                configuration[base_word]['aspekt'][done]['forma'][forma]['liczba'][liczba]['osoba'] = {}
                for osoba in ['pierwsza', 'druga', 'trzecia']:
                    configuration[base_word]['aspekt'][done]['forma'][forma]['liczba'][liczba]['osoba'][osoba] = {}
                    conj = schema.Schema()
                    if forma == 'czas przeszly':
                        try:
                            for rodzaj in ['meski', 'zenski', 'nijaki']:
                                configuration[base_word]['aspekt'][done]['forma'][forma]['liczba'][liczba]['osoba'][osoba][rodzaj] = conj.get_word_past(config['koniugacja'], forma, liczba, rodzaj, osoba, base_word)
                        except Exception:
                            pass
                    else:
                        configuration[base_word]['aspekt'][done]['forma'][forma]['liczba'][liczba]['osoba'][osoba] =  conj.get_word_present(config['koniugacja'],forma, liczba, osoba, base_word)
        
        self.database.save_verb(configuration[base_word], base_word)
        return configuration[base_word]

            
    def __get_conf_adjective(self, base_word, data):
        if len(data) == 0:
            raise Exception("adjective error")
        words = data[0].replace("|", "").split("\n")
        
        assert len(words) > 0
        word = words[0]
        
        last_letter = base_word[len(base_word) - 1]
        
        if last_letter == 'y' or last_letter == 'i':
            configuration = copy.deepcopy(schema.adjective_schema[last_letter])
            for przypadek in configuration['przypadek']:
                for liczba in configuration['przypadek'][przypadek]['liczba']:
                    for rodzaj in configuration['przypadek'][przypadek]['liczba'][liczba]['rodzaj']:
                        configuration['przypadek'][przypadek]['liczba'][liczba]['rodzaj'][rodzaj] = base_word[0:len(base_word) - 1] + configuration['przypadek'][przypadek]['liczba'][liczba]['rodzaj'][rodzaj] 

        configuration = { 'stopien' : { 'podstawowy' : configuration } }
        return configuration

    def get_conf(self, word):
        data = self._get_conf(word)

        type = re.findall("-([^-]*)-polski", data)
        if len(type) == 0:
            raise Exception("word not found")
        return {
            'przymiotnik': self.__get_conf_adjective,
            'czasownik': self.__get_conf_verb,
            'rzeczownik': self.__get_conf_noun  #
        }.get(type[0])(word, re.findall("\{\{odmiana-" + type[0] + "-polski([^\}]*)}}", data));

    def get_word(self, conf):
        '''
            Conf is a configuration that user chose to get information about word.
            It's a touple, that first element determines type of word, second is the word alone,
            and the third is a dictionary that contains details about form of word we want to have
        
        '''
        word_about = self._get_conf(conf[1])
        
        try:
            return self.database.get_word(conf[2], conf[1])
        except:
            try:
                if conf[0] == 'przymiotnik':
                    tmp = self.__get_conf_adjective(conf[1], re.findall("\{\{odmiana-przymiotnik-polski([^\}]*)}}", word_about))['stopien'][conf[2]['stopień']]['przypadek'][conf[2]['przypadek']]['liczba'][conf[2]['liczba']]['rodzaj'][conf[2]['rodzaj']],  #
                    tmp = tmp[0]
                    return tmp
                elif conf[0] == 'czasownik':
                    return self.__get_conf_verb(conf[1], re.findall("\{\{odmiana-czasownik-polski([^\}]*)}}", word_about))['aspekt'][conf[2]['aspekt']]['forma'][conf[2]['forma']]['liczba'][conf[2]['liczba']]['osoba'][conf[2]['osoba']]
                elif conf[0] == 'rzeczownik': 
                    return self.__get_conf_noun(conf[1], re.findall("\{\{odmiana-rzeczownik-polski([^\}]*)\}\}", word_about))['przypadek'][conf[2]['przypadek']]['liczba'][conf[2]['liczba']]
            except KeyError, Exception:
                return 'No information about this form'
        

    def get_dump(self, word=None, conf=None):
        return self._get_dump(word, conf)







