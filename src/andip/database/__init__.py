# -*- coding: utf-8 -*-

from andip.default import DefaultProvider
from dbStorage import DbStorage

class DatabaseProvider(DefaultProvider):
    def __init__(self, path, backoff = None):
        self.database = DbStorage(path)
        self.__backoff = backoff

    def _get_word(self, conf):
        '''
        Returns word or throw KeyError, if there is no information
        about word in database
        '''
        if not self.database:
            raise IOError("Unable to access the database (closed?)")

        return self.database.get_word(conf[2], conf[1])

    def _get_conf(self, word):
        '''
        Returns word configuration or KeyError, if there is no
        information about word in database
        '''
        if not self.database:
            raise IOError("Unable to access the database (closed?)")

        print 'aaa'

        return self.database.get_conf_preview(word)

    def save(self, conf):
        if not self.database:
            raise IOError("Unable to access the database (closed?)")

        self.database.save(conf[2], conf[1], conf[0])

    def close(self):
        self.database.close()
        self.database = None
