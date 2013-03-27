import urllib
import re
import copy

from andip import DataProvider
from andip.database import Database

class DatabaseProvider(DataProvider):
    
    def __init__(self, url):
        self.database = Database(url)
    
    def get_word(self, conf):
        '''
            Returns word or throw KeyError, if there is no information
            about word in database
        '''
        return self.database.get_conf(conf[1])
    
    def get_conf(self, word):
        '''
            Returns word configuration or KeyError, if there is no
            information about word in database
        '''
        return self.database.get_conf(word)