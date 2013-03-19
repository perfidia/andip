# -*- coding: utf-8 -*-
'''
Created on Apr 27, 2012

@author: Mateusz Dembski
'''

from persistent.mapping import PersistentMapping
import transaction

class DatabaseProvider(object):
    
    def __init__(self, name):
        storage = FileStorage('../data/' + name + '.fs')
        db = DB(storage)
        connection = db.open()
        self.root = connection.root()

    def _dictionary_init(self):
       '''
           Initialization of database dictionaries.
       '''
       self.root['przymiotnik'] = {} # tutaj uzupe³nij, jeœli potrzebujesz coœ wiêcej do s³ownika
       self.root['rzeczownik'] = {} # tutaj uzupe³nij, jeœli potrzebujesz coœ wiêcej do s³ownika
       self.root['czasownik'] = {'word' : {} }

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
            return self.root['czasownik']['word'][base_word]['aspekt'][conf[2]['aspekt']][conf[2]['forma']]['liczba'][conf[2]['liczba']]['osoba'][conf[2]['osoba']];
        except KeyError:
            raise Exception("Key Error occured");


    

