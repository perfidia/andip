#-*- coding: utf-8 -*-
'''
Created on Apr 27, 2012

@author: Bartosz Alchimowicz
'''

import urllib
import re

from andip import DataProvider
from andip.provider import Conjugation


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
        
    def _get_dump(self, word = None, conf = None):
        """
        Dump data of a specified word in a string recognazible by FileProvider.
        @param word: a word to dump
        @param conf: restric dump to a specified configuration
        @return: string in a JSON format
        """
        pass

    
class PlWikiProvider(WikiProvider):
    
    def __init__(self):
        WikiProvider.__init__(self, "http://pl.wiktionary.org/")
        self.__schema_adjective = None
    
    def _load(self, data_set):
        return eval(open(data_set + ".txt").read())
    
    def __get_conf_verb(self, data):
        if len(data) == 0:
            raise Exception("verb error")
        for conf in data:
            config = dict()
            conf = conf.replace("| ", "").split("\n")
            for element in filter(None, conf): # filter removes empty elements
                tmp = element.split("=")
                config[tmp[0]] = tmp[1]
            return config
                
    def __get_conf_noun(self, data):
        print 'noun'
            
    def __get_conf_adjective(self, data):
        if len(data) == 0:
            raise Exception("adjective error")
        words = data[0].replace("|", "").split("\n")
        
        assert len(words) > 0
        word = words[0]
        
        # generowanie stopniowania
        if word == '' or word == 'brak':
            # brak stopniowania?
            return
        else:
#            print word # stopniowanie na podstawie podanego drugiego stopnia
            pass
    
        # generowanie odmian
        if self.__schema_adjective is None:
            self.__schema_adjective = self._load("../data/adjective_schema")

        last_letter = word[len(word) - 1]
        if last_letter == 'y' or last_letter == 'i':
            retval = self.__schema_adjective[last_letter]
            for przyp in retval['przypadek']:
                for licz in retval['przypadek'][przyp]['liczba']:
                    for rodz in retval['przypadek'][przyp]['liczba'][licz]['rodzaj']:
                        retval['przypadek'][przyp]['liczba'][licz]['rodzaj'][rodz] = word[0:len(word) - 2] + retval['przypadek'][przyp]['liczba'][licz]['rodzaj'][rodz] 
                    
        return retval
#        print self.__schema_adjective['y']
        
#        retval = self.conf_cache.get(word, None)


    def get_conf(self, word):
        data = self._get_conf(word)

        type = re.findall("-([^-]*)-polski", data)
        if len(type) == 0:
            raise Exception("word not found")
        return {
            'przymiotnik': self.__get_conf_adjective,
            'czasownik': self.__get_conf_verb,
            #(re.findall("\{\{odmiana-czasownik-polski([^\}]*)}}", data)),
            'rzeczownik': self.__get_conf_noun #
        }.get(type[0])(re.findall("\{\{odmiana-" + type[0] + "-polski([^\}]*)}}", data));

    def get_word(self, conf):
        '''
            Conf is a configuration that user chose to get information about word.
            It's a touple, that first element determines type of word, second is the word alone,
            and the third is a dictionary that contains details about form of word we want to have
        
        '''
        word_about =  self._get_conf(conf[1])
        
        if conf[0] == 'przymiotnik':
            tmp = self.__get_conf_adjective(word_about), #
        elif conf[0] == 'czasownik': 
            tmp = self.__get_conf_verb(re.findall("\{\{odmiana-czasownik-polski([^\}]*)}}", word_about)),
            tmp = tmp[0]
            
            conj = Conjugation.Conjugation(Conjugation.conjugation[tmp['koniugacja']], tmp['dokonany'])
            new_end = conj.get_word(conf[2]['forma'], conf[2]['liczba'], conf[2]['osoba'])
            
            return conf[1].replace(conj.end, new_end)
        elif conf[0] == 'rzeczownik': 
            tmp =  self.__get_conf_noun #
            
        
        

    def get_dump(self, word = None, conf = None):
        return self._get_dump(word, conf)







