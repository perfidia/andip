# -*- coding: utf-  8 -*-

import copy

from andip.default import DefaultProvider

class FileProvider(DefaultProvider):
    def __init__(self, filename, backoff = None):
        DefaultProvider.__init__(self, backoff)
        self.data_set = self.__load(filename)
        self.conf_cache = None

    def __load(self, data_set):
        return eval(open(data_set + ".txt").read())

    def __get_word(self, properties, data):
        assert len(data.keys()) == 1

        key = data.keys()[0]
        val = properties[key]
        data = data[key]

        if data.has_key(val):
            data = data[val]
        else:
            raise LookupError("data not found, searched for = %s, available = %s" % (val, data))

        del properties[key]

        if isinstance(data, basestring):
            return data

        if len(properties.keys()) == 0:
            #raise Exception("incorrect path: %s", data)
            return data

        return self.__get_word(properties, data)

    def __build_cache_travel(self, data, past):
        if isinstance(data, basestring):
            tmp = (past[0], past[1], past[2])

            if not self.conf_cache.has_key(data):
                self.conf_cache[data] = []

            self.conf_cache[data].append(tmp)

            return

        assert len(data.keys()) == 1

        k = data.keys()[0]

        for v in data[k]:
            c = copy.deepcopy(past)
            c[2][k] = v

            self.__build_cache_travel(data[k][v], c)

    def __build_cache(self):
        self.conf_cache = dict()

        for part in self.data_set:
            for word in self.data_set[part]['word']:
                self.__build_cache_travel(self.data_set[part]['word'][word], [part, word, {}])

    def _get_word(self, conf):

        part, base, properties = conf
        data = self.data_set[part]['word'][base]

        if isinstance(data, dict):
            tmp = dict(properties) # copy, since _get_word removes fields

            retval = self.__get_word(tmp, data)
        else:
            retval = data

        return retval

    def _get_conf(self, word):
        assert isinstance(word, str)

        if self.conf_cache is None:
            self.__build_cache()

        retval = self.conf_cache.get(word, None)
        if retval == None:
            raise LookupError('configuration not found')

        return retval