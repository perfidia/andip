import urllib
import re
import copy

from andip import DataProvider
from andip.provider.database import Database

class DatabaseProvider(DataProvider):
    def __init__(self, url):
        self.database = Database(url)

    def get_word(self, conf):
        '''
        Returns word or throw KeyError, if there is no information
        about word in database
        '''
        if not self.database:
            raise IOError("Unable to access the database (closed?)")

        return self.database.get_word(conf[2], conf[1])

    def get_conf(self, word):
        '''
        Returns word configuration or KeyError, if there is no
        information about word in database
        '''
        if not self.database:
            raise IOError("Unable to access the database (closed?)")

        return self.database.get_conf(word)

    def save(self, conf):
        if not self.database:
            raise IOError("Unable to access the database (closed?)")

        self.database.save(conf[2], conf[1], conf[0])

    def close(self):
        self.database.close()

        self.database = None
