# -*- coding: utf-8 -*-

class DefaultProvider(object):

    def get_word(self, conf):
        """
        Get a specified word from a dictionary.

        @param conf a tuple build from three parts:
        - part of a speech,
        - base word,
        - dict of properties.

        @return word in a specified configuration
        """
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
        raise NotImplementedError("abstract method")

    def test_configuration_format(self, conf):
        """
        Function test whether the configuration dictionary is build well.

        Each configuration should be a tuple build from three parts:
        - part of a speech,
        - base word,
        - dict of properties.

        @return a list with configurations
        """

        raise AttributeError("Configuration test failed!")