# -*- coding: utf-8 -*-

class DefaultProvider(object):

    def __init__(self, backoff):
        self.__backoff = backoff

    def get_word(self, conf):
        """Get a specified word from a dictionary.

        Each configuration is a tuple build from three parts:
        * part of a speech,
        * base word,
        * dict of properties.

        :param conf: configuration of a word
        :type conf: tuple built from the following elements: part of a speech(str), base word(str), properties(dict)

        :return: word in a specified configuration
        :rtype: str

        :raises LookupError: if word not found

        >>> from andip import FileProvider
        >>> p = FileProvider("../data/polish")
        >>> print p.get_word(("czasownik", "następować", {'aspekt': 'dokonane', 'forma': 'czas teraźniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'}))
        następują
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
        """Get configurations for a given word.

        :param word: item for which configuration is required
        :type word: str

        :returns: a list with configurations, see :class:`DefaultProvider.get_word`
        :rtype: list of tuples

        :raises LookupError: if word not found

        >>> from andip import FileProvider
        >>> p = FileProvider("../data/polish")
        >>> print p.get_conf('występują')
        [('czasownik', 'wyst\xc4\x99powa\xc4\x87', {'forma': 'czas tera\xc5\xbaniejszy', 'osoba': 'trzecia', 'aspekt': 'niedokonane', 'liczba': 'mnoga'})]
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