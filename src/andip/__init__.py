# -*- coding: utf-8 -*-

class AnDiP(object):
    def __init__(self, provider, backoff = None):
        assert isinstance(provider, DataProvider)

        self.__provider = provider
        self.__backoff = backoff;
        self.__unsaved_items = list()

    def get_word(self, conf):
        """
        Get a specified word from a dictionary.

        @param conf a tuple build from three parts: part of a speech, base word and dict of properties

        @return word in a specified configuration
        """

        try:
            retval = self.__backoff.get_word(conf)
        except Exception:
            retval = self.__provider.get_word(conf)

        if isinstance(retval, tuple):
            self.__unsaved_items.append(retval[1])
            return retval[0]
        else:
            return retval

    def get_conf(self, word):
        """
        Get the configuration for a given word.

        Each configuration is a tuple build from three parts:
        - part of a speech
        - base word
        - dict of properties

        @return a list with configurations
        """

        try:
            return self.__backoff.get_conf(word)
        except Exception:
            return self.__provider.get_conf(word)

    def save(self, items = None):
        """
        Saves all unsaved items using all providers including backoff.
        """
        if items == None:
            self.__backoff.save(self.__unsaved_items)
        else:
            for item in items:
                self.__provider.save(item)

class DataProvider(object):
    def get_word(self, conf):
        raise NotImplementedError("abstract method")

    def get_conf(self, word):
        raise NotImplementedError("abstract method")

    def save(self):
        raise NotImplementedError("abstract method")
