# -*- coding: utf-8 -*-

import unittest
from andip import AnDiP
from andip.provider import PlWikiProvider

class WikiPolishTest(unittest.TestCase):
    
    def setUp(self):
        self.wiki = PlWikiProvider("../data/polish")
        self.ad = AnDiP(self.wiki)
        
    def tearDown(self):
        pass
        
    def test_verb_get_conf(self):
        self.assertEquals('występują', self.ad.get_word(('czasownik', 'występować', {'aspekt' : 'niedokonane', 'forma' : 'czas terazniejszy', 'liczba' : 'mnoga', 'osoba': 'trzecia'})))
        self.assertEquals('występuje', self.ad.get_word(('czasownik', 'występować', {'aspekt' : 'niedokonane', 'forma' : 'czas terazniejszy', 'liczba' : 'pojedyncza', 'osoba': 'trzecia'})))
        self.assertEquals('występujemy', self.ad.get_word(('czasownik', 'występować', {'aspekt' : 'niedokonane', 'forma' : 'czas terazniejszy', 'liczba' : 'mnoga', 'osoba': 'pierwsza'})))
        self.assertEquals('występujecie', self.ad.get_word(('czasownik', 'występować', {'aspekt' : 'niedokonane', 'forma' : 'czas terazniejszy', 'liczba' : 'mnoga', 'osoba': 'druga'})))
        self.assertEquals('występujesz', self.ad.get_word(('czasownik', 'występować', {'aspekt' : 'niedokonane', 'forma' : 'czas terazniejszy', 'liczba' : 'pojedyncza', 'osoba': 'druga'})))
        
    def test_adjective_get_conf(self):
        self.assertEquals('zachodnich', self.ad.get_word(('przymiotnik', 'zachodni', {'stopień': 'podstawowy', 'przypadek' : 'dopełniacz', 'liczba': 'mnoga', 'rodzaj': 'm'})))
        self.assertEquals('zachodniego', self.ad.get_word(('przymiotnik', 'zachodni', {'stopień': 'podstawowy', 'przypadek' : 'biernik', 'liczba': 'pojedyńcza', 'rodzaj': 'm'})))
        self.assertEquals('zachodniego', self.ad.get_word(('przymiotnik', 'zachodni', {'stopień': 'podstawowy', 'przypadek' : 'dopełniacz', 'liczba': 'pojedyńcza', 'rodzaj': 'm'})))
        self.assertEquals('zachodnim', self.ad.get_word(('przymiotnik', 'zachodni', {'stopień': 'podstawowy', 'przypadek' : 'miejscownik', 'liczba': 'pojedyńcza', 'rodzaj': 'm'})))
        self.assertEquals('zachodniej', self.ad.get_word(('przymiotnik', 'zachodni', {'stopień': 'podstawowy', 'przypadek' : 'miejscownik', 'liczba': 'pojedyńcza', 'rodzaj': 'ż'})))

        # stopniowanie
        self.assertEquals('żółtszych', self.ad.get_word(('przymiotnik', 'żółty', {'przypadek' : 'dopełniacz', 'stopień' : 'wyższy', 'liczba': 'mnoga', 'rodzaj': 'm'})))
        self.assertEquals('żółtszym', self.ad.get_word(('przymiotnik', 'żółty', {'przypadek' : 'celownik', 'stopień' : 'wyższy', 'liczba': 'mnoga', 'rodzaj': 'm'})))
        self.assertEquals('najżółtszych', self.ad.get_word(('przymiotnik', 'żółty', {'przypadek' : 'dopełniacz', 'stopień' : 'najwyższy', 'liczba': 'mnoga', 'rodzaj': 'm'})))
        self.assertEquals('najżółtszym', self.ad.get_word(('przymiotnik', 'żółty', {'przypadek' : 'celownik', 'stopień' : 'najwyższy', 'liczba': 'mnoga', 'rodzaj': 'm'})))
