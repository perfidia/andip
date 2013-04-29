# -*- coding: utf-8 -*-

class DefaultProvider(object):

    def __init__(self, backoff):
        self.__backoff = backoff

    def get_word(self, conf):
        """
        Get a specified word from a dictionary.

        @param conf a tuple build from three parts:
        - part of a speech,
        - base word,
        - dict of properties.

        @return word in a specified configuration
        """
        try:
            assert isinstance(conf, tuple)
            assert len(conf) == 3
            assert isinstance(conf[0], basestring)
            assert isinstance(conf[1], basestring)
            assert isinstance(conf[2], dict)
        except AssertionError:
            raise AttributeError("Configuration test failed!")
        else:
            try:
                return self._get_word(conf)
            except Exception:
                if (self.__backoff):
                    return self.__backoff._get_word(conf)
                else:
                    raise LookupError('word not found')

            # if isinstance(retval, tuple):
            #     return retval[0]
            # else:
            #     return retval

    def _get_word(self, conf):
        raise NotImplementedError("abstract method")

    def get_conf(self, word):
        """
        Get the configuration for a given word.

        Each configuration is a tuple build from three parts:
        - part of a speech,
        - base word,
        - dict of properties.

        @return a list with configurations
        """
        try:
            assert isinstance(word, basestring)
        except AssertionError:
            raise AttributeError("Configuration test failed!")
        else:
            try:
                return self._get_conf(word)
            except Exception:
                if (self.__backoff):
                    return self.__backoff._get_conf(word)
                else:
                    raise LookupError('configuration not found')

    def _get_conf(self, word):
        raise NotImplementedError("abstract method")
