# -*- coding: utf-8 -*-

import unittest
from andip import AnDiP
from andip.provider import PlWikiProvider

class WikiPolishTest(unittest.TestCase):
    
    def setUp(self):
        self.ad = AnDiP(PlWikiProvider())
        
    def test_verb_get_conf(self):
        self.assertEquals('występują', self.ad.get_word(('czasownik', 'występować', {'aspekt' : 'niedokonane', 'forma' : 'czas terazniejszy', 'liczba' : 'mnoga', 'osoba': 'trzecia'})))
        self.assertEquals('występuje', self.ad.get_word(('czasownik', 'występować', {'aspekt' : 'niedokonane', 'forma' : 'czas terazniejszy', 'liczba' : 'pojedyncza', 'osoba': 'trzecia'})))
        self.assertEquals('występujemy', self.ad.get_word(('czasownik', 'występować', {'aspekt' : 'niedokonane', 'forma' : 'czas terazniejszy', 'liczba' : 'mnoga', 'osoba': 'pierwsza'})))
        self.assertEquals('występujecie', self.ad.get_word(('czasownik', 'występować', {'aspekt' : 'niedokonane', 'forma' : 'czas terazniejszy', 'liczba' : 'mnoga', 'osoba': 'druga'})))
        self.assertEquals('występujesz', self.ad.get_word(('czasownik', 'występować', {'aspekt' : 'niedokonane', 'forma' : 'czas terazniejszy', 'liczba' : 'pojedyncza', 'osoba': 'druga'})))