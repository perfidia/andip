import urllib
import re
import copy

from andip import DataProvider
from andip.database import Database
from andip.provider import FileProvider, PlWikiProvider, DatabaseProvider

class BackoffProvider(DataProvider):
    
    def get_word(self, conf):
        '''
            Returns word or throw KeyError, if there is no information
            about word in database
        '''
        # Try get data from Database
        try:
            provider = FileProvider("../data/polish")
            return provider.get_word(conf)
        except:
            try:
                provider = PlWikiProvider("../data/Polish")
                return provider.get_word(conf)
            except:
                raise KeyError("There is no such word in AnDiP services")
            
    
    def get_conf(self, word):
        '''
            Returns word configuration or KeyError, if there is no
            information about word in database
        '''
        try:
            provider = FileProvider("../data/polish")
            return provider.get_conf(word)
        except:
            try:
                provider = PlWikiProvider("../data/Polish")
                return provider.get_conf(word)
            except:
                raise KeyError("There is no such word in AnDiP services")