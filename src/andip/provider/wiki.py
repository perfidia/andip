'''
Created on Apr 27, 2012

@author: Bartosz Alchimowicz
'''

import copy
import collections

from andip import DataProvider

class WikiProvider(DataProvider):
    def __init__(self, url):
        self.url = url
        
#    def _get_word(self, properties, data):
#        assert len(data.keys()) == 1
#
#        key = data.keys()[0]
#        val = properties[key]
#        data = data[key]
#
#        if data.has_key(val):
#            data = data[val]
#        else:
#            raise Exception("data not found, searched for = %s, available = %s" % (val, data))
#
#        del properties[key]
#
#        if isinstance(data, basestring):
#            return data
#
#        if len(properties.keys()) == 0:
#            #raise Exception("incorrect path: %s", data)
#            return data
#
#        return self._get_word(properties, data)
#
#    def _build_cache_travel(self, data, past):
#        if isinstance(data, basestring):
#            tmp = (past[0], past[1], past[2])
#
#            if not self.conf_cache.has_key(data):
#                self.conf_cache[data] = []
#
#            self.conf_cache[data].append(tmp)
#
#            return
#
#        assert len(data.keys()) == 1
#
#        k = data.keys()[0]
#
#        for v in data[k]:
#            c = copy.deepcopy(past)
#            c[2][k] = v
#
#            self._build_cache_travel(data[k][v], c)
#
#    def _build_cache(self):
#        self.conf_cache = dict()
#
#        for part in self.data_set:
#            for word in self.data_set[part]['word']:
#                self._build_cache_travel(self.data_set[part]['word'][word], [part, word, {}])

    def get_word(self, conf):
        assert isinstance(conf, tuple)
        assert len(conf) == 3
        assert isinstance(conf[0], basestring)
        assert isinstance(conf[1], basestring)
        assert isinstance(conf[2], dict)

        part, base, properties = conf

#        data = self.data_set[part]['word'][base]
        
#        switch = {
#            'przymiotnik': 'one',
#            'czasownik': 'two'
#        }.get(properties[0], 'n/a')();


#        if isinstance(data, dict):
#            tmp = dict(properties) # copy, since _get_word removes fields
#
#            retval = self._get_word(tmp, data)
#        else:
#            retval = data
#
#        return retval

    def get_conf(self, word):
        assert isinstance(word, str)

#        if self.conf_cache is None:
#            self._build_cache()
#
#        retval = self.conf_cache.get(word, None)
#
#        return retval
    
    def get_dump(self, word = None, conf = None):
        """
        Dump data of a specified word in a string recognazible by FileProvider.
        @param word: a word to dump
        @param conf: restric dump to a specified configuration
        @return: string in a JSON format
        """
        pass

    
class PlWikiProvider(WikiProvider):
    def __init__(self):
        WikiProvider.__init__(self, "http://pl.wiktionary.org/...")

