# -*- coding: utf-8 -*-
'''
Created on Apr 27, 2012

@author: Mateusz Dembski
'''

from ZODB.FileStorage import FileStorage
from ZODB.DB import DB
from persistent.mapping import PersistentMapping
import transaction

class Database(object):
    
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

    def save_verb(self, dict, base_word):
        '''
            Save verb to database in Bartosz Alchimowicz convention
        '''
        self.root['czasownik']['word'][base_word] = dict
        transaction.commit()

    def save_adjective(self, dict, base_word):
        '''
            Save verb to database in Bartosz Alchimowicz convention
        '''
        self.root['przymiotnik']['word'][base_word] = dict
        transaction.commit()

    def save_noun(self, dict, base_word):
        '''
            Save noun to database in Bartosz Alchimowicz convention
        '''
        self.root['rzeczownik']['word'][base_word] = dict
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
                    
        
        
        
        
        