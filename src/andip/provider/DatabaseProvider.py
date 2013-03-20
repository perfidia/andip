# -*- coding: utf-8 -*-
'''
Created on Apr 27, 2012

@author: Mateusz Dembski
'''

from ZODB.FileStorage import FileStorage
from ZODB.DB import DB
from persistent.mapping import PersistentMapping
import transaction

class DatabaseProvider(object):
    
    def __init__(self, name):
        storage = FileStorage('../data/' + name + '.fs')
        db = DB(storage)
        connection = db.open()
        self.root = connection.root()
        if not self.root:
            self._dictionary_init()

    def _dictionary_init(self):
       '''
           Initialization of database dictionaries.
       '''
       self.root['przymiotnik'] = PersistentMapping() # tutaj uzupe�nij, je�li potrzebujesz co� wi�cej do s�ownika
       self.root['rzeczownik'] = PersistentMapping() # tutaj uzupe�nij, je�li potrzebujesz co� wi�cej do s�ownika
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

    def get_verb(self, conf, base_word):
        '''
            Get verb using configuration
        '''
        try:
            return self.root['czasownik']['word'][base_word]['aspekt'][conf['aspekt']][conf['forma']]['liczba'][conf['liczba']]['osoba'][conf['osoba']]
        except KeyError:
            raise Exception("Key Error occured")

    def save_adjective(self, dict, base_word):
        '''
            Save verb to database in Bartosz Alchimowicz convention
        '''
        self.root['przymiotnik']['word'][base_word] = dict
        transaction.commit()

    def get_adjective(self, conf, base_word):
        '''
            Get verb using configuration
        '''
        try:
            return self.root['przymiotnik']['word'][base_word]['stopień'][conf['stopień']]['przypadek'][conf['przypadek']]['liczba'][conf['liczba']]['rodzaj'][conf['rodzaj']]
        except KeyError:
            raise Exception("Key Error occured")


    

