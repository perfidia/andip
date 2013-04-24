# -*- coding: utf-8 -*-

class DefaultProvider(object):
    def get_word(self, conf):
        raise Exception("abstract method")

    def get_conf(self, word):
        raise Exception("abstract method")

    def save(self):
        raise Exception("abstract method")