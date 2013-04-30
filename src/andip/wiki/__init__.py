# -*- coding: utf-8 -*-

import urllib
import re
import copy

from andip.default import DefaultProvider
from schema import Schema

class WikiProvider(DefaultProvider):
    def __init__(self, url, backoff):
        DefaultProvider.__init__(self, backoff)
        self.__url = url
        self.__buffered_data = dict()

    def get_model(self):
        """
        This function is supported only by WikiProvider.
        Wikiprovider store data downloaded from wiktionary.org.

        Use this function to get this data so you can add it to database using DatabaseProvider.
        @return buffered data
        """
        return self.__buffered_data

    def _get_conf(self, word):
        # from buffer
        pass

    def _get_word(self, conf):
        if (self.__buffered_data.has_key(conf[1])):
            # if conf[2].hasKey('forma') and conf[2]['forma'] == 'czas terazniejszy':
            #     del conf[2]['rodzaj']
            return self._get_word_from_buffer(conf[2], copy.deepcopy(self.__buffered_data[conf[1]]))
        else:
            return self._get_word_from_api(conf)[0]

    def _get_word_from_api(self, conf):
        raise NotImplementedError("abstract method")

    def _get_word_from_buffer(self, properties, data):
        # print properties
        # print data
        # print

        assert len(data.keys()) == 1

        key = data.keys()[0]
        val = properties[key]
        data = data[key]

        if data.has_key(val):
            data = data[val]
        else:
            raise LookupError("data not found")

        del properties[key]

        if isinstance(data, basestring):
            return data

        if len(properties.keys()) == 0:
            #raise Exception("incorrect path: %s", data)
            return data

        return self._get_word_from_buffer(properties, data)

    def _add_to_buffer(self, conf):
        self.__buffered_data[conf[1]] = conf[2]

    def _get_data_from_api(self, word):
        assert isinstance(word, str)

        return urllib.urlopen(self.__url + 'w/api.php?format=xml&action=query&prop=revisions&rvprop=content&titles=' + word).read()


class PlWikiProvider(WikiProvider):
    def __init__(self, backoff = None):
        WikiProvider.__init__(self, "http://pl.wiktionary.org/", backoff)
        self.__schema = Schema()

    def __get_conf_noun(self, base_word, data):
        configuration = {}
        configuration[base_word] = {}
        configuration[base_word]['przypadek'] = {}

        for przypadek in ['mianownik', 'dopełniacz', 'celownik', 'biernik', 'narzędnik', 'miejscownik', 'wołacz']:
            configuration[base_word]['przypadek'][przypadek] = {}
            configuration[base_word]['przypadek'][przypadek]['liczba'] = {}

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
            return configuration[base_word]

    def __get_conf_verb(self, base_word, data):
        if len(data) == 0:
            raise LookupError("verb error")

        conf = data[0]
        config = dict()
        conf = conf.replace("|", "").split("\n")
        for element in filter(None, conf):  # filter removes empty elements
            tmp = element.replace(" ", "").split("=")
            config[tmp[0]] = tmp[1]

        if config['dokonany'] == 'tak':
            done = 'dokonane'
        else:
            done = 'niedokonane'

        if 'koniugacja' not in config.keys():
            return self.__generate_from_wiki(config, base_word, done)

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
                    conj = self.__schema
                    if forma == 'czas przeszly':
                        configuration[base_word]['aspekt'][done]['forma'][forma]['liczba'][liczba]['osoba'][osoba]['rodzaj'] = {}
                        try:
                            for rodzaj in ['meski', 'zenski', 'nijaki']:
                                configuration[base_word]['aspekt'][done]['forma'][forma]['liczba'][liczba]['osoba'][osoba]['rodzaj'][rodzaj] = conj.get_word_past(config['koniugacja'], forma, liczba, rodzaj, osoba, base_word)
                        except Exception:
                            pass
                    else:
                        configuration[base_word]['aspekt'][done]['forma'][forma]['liczba'][liczba]['osoba'][osoba] =  conj.get_word_present(config['koniugacja'],forma, liczba, osoba, base_word)

        return configuration[base_word]


    def __get_conf_adjective(self, base_word, data):

        last_letter = base_word[len(base_word) - 1]
        if len(data) == 0 or (last_letter != 'y' and last_letter != 'i'):
            raise LookupError("adjective not found")

        words = data[0].replace("|", "").split("\n")
        assert len(words) > 0
        word = words[0]

        # stopień podstawowy
        configuration = copy.deepcopy(self.__schema.adjective_schema[last_letter])
        for przypadek in configuration['przypadek']:
            for liczba in configuration['przypadek'][przypadek]['liczba']:
                for rodzaj in configuration['przypadek'][przypadek]['liczba'][liczba]['rodzaj']:
                    configuration['przypadek'][przypadek]['liczba'][liczba]['rodzaj'][rodzaj] = base_word[0:len(base_word) - 1] + configuration['przypadek'][przypadek]['liczba'][liczba]['rodzaj'][rodzaj]
        configuration_basic = copy.deepcopy(configuration)

        if word == 'brak' or word == '':
            return { 'stopień' : { 'podstawowy' : configuration_basic } }

        # stopień wyższy
        configuration = copy.deepcopy(self.__schema.adjective_schema[last_letter])
        for przypadek in configuration['przypadek']:
            for liczba in configuration['przypadek'][przypadek]['liczba']:
                for rodzaj in configuration['przypadek'][przypadek]['liczba'][liczba]['rodzaj']:
                    configuration['przypadek'][przypadek]['liczba'][liczba]['rodzaj'][rodzaj] = word[0:len(word) - 1] + configuration['przypadek'][przypadek]['liczba'][liczba]['rodzaj'][rodzaj]
        configuration_higher = copy.deepcopy(configuration)

        # stopień najwyższy
        for przypadek in configuration['przypadek']:
            for liczba in configuration['przypadek'][przypadek]['liczba']:
                for rodzaj in configuration['przypadek'][przypadek]['liczba'][liczba]['rodzaj']:
                    configuration['przypadek'][przypadek]['liczba'][liczba]['rodzaj'][rodzaj] = 'naj' + configuration['przypadek'][przypadek]['liczba'][liczba]['rodzaj'][rodzaj]
        configuration_the_highest = copy.deepcopy(configuration)

        return { 'stopień' : {'podstawowy' : configuration_basic,
                              'wyższy' : configuration_higher,
                              'najwyższy' : configuration_the_highest  } }

    def _get_word_from_api(self, conf):
        word_about = self._get_data_from_api(conf[1])

        # try:
        if conf[0] == 'przymiotnik':
            fullconf = ('przymiotnik', conf[1], self.__get_conf_adjective(conf[1], re.findall("\{\{odmiana-przymiotnik-polski([^\}]*)}}", word_about)))
            self._add_to_buffer(fullconf)
            return (fullconf[2]['stopień'][conf[2]['stopień']]['przypadek'][conf[2]['przypadek']]['liczba'][conf[2]['liczba']]['rodzaj'][conf[2]['rodzaj']], fullconf)
        elif conf[0] == 'czasownik':
            fullconf = ('czasownik', conf[1], self.__get_conf_verb(conf[1], re.findall("\{\{odmiana-czasownik-polski([^\}]*)}}", word_about)))
            self._add_to_buffer(fullconf)
            if conf[2]['forma'] == 'czas terazniejszy':
                return (fullconf[2]['aspekt'][conf[2]['aspekt']]['forma'][conf[2]['forma']]['liczba'][conf[2]['liczba']]['osoba'][conf[2]['osoba']], fullconf)
            else:
                return (fullconf[2]['aspekt'][conf[2]['aspekt']]['forma'][conf[2]['forma']]['liczba'][conf[2]['liczba']]['osoba'][conf[2]['osoba']]['rodzaj'][conf[2]['rodzaj']], fullconf)
        elif conf[0] == 'rzeczownik':
            fullconf = ('rzeczownik', conf[1], self.__get_conf_noun(conf[1], re.findall("\{\{odmiana-rzeczownik-polski([^\}]*)\}\}", word_about)))
            self._add_to_buffer(fullconf)
            return (fullconf[2]['przypadek'][conf[2]['przypadek']]['liczba'][conf[2]['liczba']], fullconf)
        # except Exception:
        raise LookupError('No information about this form')

    def __generate_from_wiki(self, config, base_word, done):

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
                    if forma == 'czas przeszly':
                        for rodzaj in ['meski', 'zenski', 'nijaki']:
                            configuration[base_word]['aspekt'][done]['forma'][forma]['liczba'][liczba]['osoba'][osoba][rodzaj] = ""
                    else:
                        configuration[base_word]['aspekt'][done]['forma'][forma]['liczba'][liczba]['osoba'][osoba] =  ""

        for word in ['robię', 'robisz', 'robi', 'robimy', 'robicie', 'robią']:
            if word in config.keys():
                if word == 'robię':
                    configuration[base_word]['aspekt'][done]['forma']['czas terazniejszy']['liczba']['pojedyncza']['osoba']['pierwsza'] = config[word]
                elif word == 'robisz':
                    configuration[base_word]['aspekt'][done]['forma']['czas terazniejszy']['liczba']['pojedyncza']['osoba']['druga'] = config[word]
                elif word == 'robi':
                    configuration[base_word]['aspekt'][done]['forma']['czas terazniejszy']['liczba']['pojedyncza']['osoba']['trzecia'] = config[word]
                elif word == 'robimy':
                    configuration[base_word]['aspekt'][done]['forma']['czas terazniejszy']['liczba']['mnoga']['osoba']['pierwsza'] = config[word]
                elif word == 'robicie':
                    configuration[base_word]['aspekt'][done]['forma']['czas terazniejszy']['liczba']['mnoga']['osoba']['druga'] = config[word]
                else:
                    configuration[base_word]['aspekt'][done]['forma']['czas terazniejszy']['liczba']['mnoga']['osoba']['trzecia'] = config[word]

        return configuration[base_word]

