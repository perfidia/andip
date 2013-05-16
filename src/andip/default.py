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
            raise ValueError("check parameters!")
        else:
            if (self.__backoff):
                try:
                    return self._get_word(conf)
                except Exception:
                    return self.__backoff.get_word(conf)
            else:
                return self._get_word(conf)

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
        if isinstance(word, basestring) == False:
            raise ValueError("check parameters!")
        else:
            if (self.__backoff):
                try:
                    return self._get_conf(word)
                except Exception:
                    return self.__backoff.get_conf(word)
            else:
                return self._get_conf(word)

    def _get_conf(self, word):
        raise NotImplementedError("abstract method")

    def get_model(self):
        raise NameError("function is not supported by this provider")

    def save_model(self):
        raise NameError("function is not supported by this provider")

    def close(self):
        raise NameError("function is not supported by this provider")