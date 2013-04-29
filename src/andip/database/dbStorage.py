# -*- coding: utf-8 -*-

from ZODB.FileStorage import FileStorage
from ZODB.DB import DB
from persistent.mapping import PersistentMapping
import transaction

class DbStorage(object):
    
    def __init__(self, name):
        self.storage = FileStorage(name + '.fs')
        self.db = DB(self.storage)
        self.connection = self.db.open()
        self.root = self.connection.root()
        if not self.root:
            self._dictionary_init()

    def close(self):
        self.connection.close()
        self.db.close()
        self.storage.close()

    def _dictionary_init(self):
        '''
           Initialization of database dictionaries.
        '''
        self.root['przymiotnik'] = PersistentMapping()
        self.root['rzeczownik'] = PersistentMapping()
        self.root['czasownik'] = PersistentMapping()
        self.root['czasownik']['word'] = PersistentMapping()
        self.root['przymiotnik']['word'] = PersistentMapping()
        self.root['rzeczownik']['word'] = PersistentMapping()
        transaction.commit()
    
    def save(self, dict, base_word, type):
        '''
            Save object to database in Bartosz Alchimowicz convention
        '''
        self.root[type]['word'][base_word] = dict
        transaction.commit()
        
    def get_conf(self, base_word):
        '''
            Get configuration of word whic is in database
        '''
        for word_type in ['rzeczownik', 'czasownik', 'przymiotnik']:
            for word in self.root[word_type]['word'].keys():
                if word == base_word:
                    return self.root[word_type]['word'][word]
                
        raise KeyError("There is no such a word in Database")

    def get_conf_preview(self, word):
        
        # rzeczownik
        dictionary = self.root['rzeczownik']['word']
        
        for base_word in dictionary.keys():
            for przypadek in dictionary[base_word]['przypadek'].keys():
                for liczba in dictionary[base_word]['przypadek'][przypadek]['liczba'].keys():
                    if dictionary[base_word]['przypadek'][przypadek]['liczba'][liczba] == word:
                        return {'type' : 'rzeczownik',
                                 'przypadek' : przypadek,
                                 'liczba' : liczba }
        # przymiotnik
        dictionary = self.root['przymiotnik']['word']
        
        for base_word in dictionary.keys():
            for stopien in dictionary[base_word]['stopień'].keys():
                for przypadek in dictionary[base_word]['stopień'][stopien]['przypadek'].keys():
                    for liczba in dictionary[base_word]['stopień'][stopien]['przypadek'][przypadek]['liczba'].keys():
                        for rodzaj in dictionary[base_word]['stopień'][stopien]['przypadek'][przypadek]['liczba'][liczba]['rodzaj'].keys():
                            if dictionary[base_word]['stopień'][stopien]['przypadek'][przypadek]['liczba'][liczba]['rodzaj'][rodzaj] == word:
                                return { 'type' : 'przymiotnik',
                                         'stopień' : stopien,
                                         'liczba' : liczba,
                                         'rodzaj' : rodzaj}
        # czasownik
        dictionary = self.root['czasownik']['word']
        
        for base_word in dictionary.keys():             
            for aspekt in dictionary[base_word]['aspekt'].keys():
                for forma in dictionary[base_word]['aspekt'][aspekt]['forma'].keys():
                    for liczba in dictionary[base_word]['aspekt'][aspekt]['forma'][forma]['liczba'].keys():
                        for osoba in dictionary[base_word]['aspekt'][aspekt]['forma'][forma]['liczba'][liczba]['osoba'].keys():
                            if forma == 'czas przeszly':
                                for rodzaj in dictionary[base_word]['aspekt'][aspekt]['forma'][forma]['liczba'][liczba]['osoba'][osoba]['rodzaj'].keys():
                                    if dictionary[base_word]['aspekt'][aspekt]['forma'][forma]['liczba'][liczba]['osoba'][osoba]['rodzaj'][rodzaj] == word:
                                        return { 'type' : 'czasownik',
                                                'aspekt' : aspekt,
                                                'forma' : forma,
                                                'liczba' : liczba,
                                                'osoba' : osoba,
                                                'rodzaj' : rodzaj}
                            else:
                                if dictionary[base_word]['aspekt'][aspekt]['forma'][forma]['liczba'][liczba]['osoba'][osoba] == word:
                                        return { 'type' : 'czasownik',
                                                'aspekt' : aspekt,
                                                'forma' : forma,
                                                'liczba' : liczba,
                                                'osoba' : osoba}
        raise LookupError("configuration not found")
            

    def get_word(self, conf, base_word):
        '''
            Search all database and get word
        '''
        
        try:
            return self.root['rzeczownik']['word'][base_word]['przypadek'][conf['przypadek']]['liczba'][conf['liczba']]
        except KeyError:
            try:
                return self.root['przymiotnik']['word'][base_word]['stopień'][conf['stopień']]['przypadek'][conf['przypadek']]['liczba'][conf['liczba']]['rodzaj'][conf['rodzaj']]
            except KeyError:
                try:
                    if conf['forma'] == 'czas terazniejszy':
                        return self.root['czasownik']['word'][base_word]['aspekt'][conf['aspekt']]['forma'][conf['forma']]['liczba'][conf['liczba']]['osoba'][conf['osoba']]
                    else:
                        return self.root['czasownik']['word'][base_word]['aspekt'][conf['aspekt']]['forma'][conf['forma']]['liczba'][conf['liczba']]['osoba'][conf['osoba']][conf['rodzaj']]
                except KeyError:
                    raise KeyError("There is no such word in Database")
                    
        
        
        
        
        