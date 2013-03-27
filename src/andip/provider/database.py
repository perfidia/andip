import urllib
import re
import copy

from andip import DataProvider
from andip.database import Database

class DatabaseProvider(DataProvider):
    
    def __init__(self, url):
        self.database = Database(url)
    
    def get_word(self, conf):
        word_result = ""
        
        # To zaraz postaram siê poprawiæ
        if conf[0] == 'przymiotnik':
            word_result = self.database.get_adjective(conf[2], conf[1])
        elif conf[0] == 'rzeczownik':
            word_result = self.database.get_noun(conf[2], conf[1])
        elif conf[0] == 'czasownik':
            word_result = self.database.get_verb(conf[2], conf[1])
        
        return word_result
    
    def get_conf(self, word):
        return self.database.get_conf(word)