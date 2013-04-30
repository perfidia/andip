# -*- coding: utf-8 -*-
import unittest
from andip import PlWikiProvider

class WikiPolishTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ad = PlWikiProvider()

    def testGetWordVerb(self):
        self.assertEquals('występują',    self.ad.get_word(('czasownik', 'występować', {'aspekt' : 'niedokonane', 'forma' : 'czas terazniejszy', 'liczba' : 'mnoga', 'osoba': 'trzecia'})))
        self.assertEquals('występuje',    self.ad.get_word(('czasownik', 'występować', {'aspekt' : 'niedokonane', 'forma' : 'czas terazniejszy', 'liczba' : 'pojedyncza', 'osoba': 'trzecia'})))
        self.assertEquals('występujemy',  self.ad.get_word(('czasownik', 'występować', {'aspekt' : 'niedokonane', 'forma' : 'czas terazniejszy', 'liczba' : 'mnoga', 'osoba': 'pierwsza'})))
        self.assertEquals('występujecie', self.ad.get_word(('czasownik', 'występować', {'aspekt' : 'niedokonane', 'forma' : 'czas terazniejszy', 'liczba' : 'mnoga', 'osoba': 'druga'})))
        self.assertEquals('występujesz',  self.ad.get_word(('czasownik', 'występować', {'aspekt' : 'niedokonane', 'forma' : 'czas terazniejszy', 'liczba' : 'pojedyncza', 'osoba': 'druga'})))

        self.assertEqual(u'jest', self.ad.get_word(('czasownik', 'być', {'aspekt' : 'niedokonane', 'forma': 'czas terazniejszy', 'liczba': 'pojedyncza', 'osoba': 'trzecia'})))
        # self.assertEqual(u'są',   self.ad.get_word(('czasownik', 'być', {'aspekt': 'niedokonane', 'forma': 'czas terazniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'})))

    def testGetWordAdjective(self):
        self.assertEquals('zachodnich',  self.ad.get_word(('przymiotnik', 'zachodni', {'stopień': 'podstawowy', 'przypadek' : 'dopełniacz', 'liczba': 'mnoga', 'rodzaj': 'm'})))
        self.assertEquals('zachodniego', self.ad.get_word(('przymiotnik', 'zachodni', {'stopień': 'podstawowy', 'przypadek' : 'biernik', 'liczba': 'pojedyńcza', 'rodzaj': 'm'})))
        self.assertEquals('zachodniego', self.ad.get_word(('przymiotnik', 'zachodni', {'stopień': 'podstawowy', 'przypadek' : 'dopełniacz', 'liczba': 'pojedyńcza', 'rodzaj': 'm'})))
        self.assertEquals('zachodnim',   self.ad.get_word(('przymiotnik', 'zachodni', {'stopień': 'podstawowy', 'przypadek' : 'miejscownik', 'liczba': 'pojedyńcza', 'rodzaj': 'm'})))
        self.assertEquals('zachodniej',  self.ad.get_word(('przymiotnik', 'zachodni', {'stopień': 'podstawowy', 'przypadek' : 'miejscownik', 'liczba': 'pojedyńcza', 'rodzaj': 'ż'})))

    def testGetWordAdjectiveComparison(self):
        self.assertEquals('żółtszych',    self.ad.get_word(('przymiotnik', 'żółty', {'przypadek' : 'dopełniacz', 'stopień' : 'wyższy', 'liczba': 'mnoga', 'rodzaj': 'm'})))
        self.assertEquals('żółtszym',     self.ad.get_word(('przymiotnik', 'żółty', {'przypadek' : 'celownik', 'stopień' : 'wyższy', 'liczba': 'mnoga', 'rodzaj': 'm'})))
        self.assertEquals('najżółtszych', self.ad.get_word(('przymiotnik', 'żółty', {'przypadek' : 'dopełniacz', 'stopień' : 'najwyższy', 'liczba': 'mnoga', 'rodzaj': 'm'})))
        self.assertEquals('najżółtszym',  self.ad.get_word(('przymiotnik', 'żółty', {'przypadek' : 'celownik', 'stopień' : 'najwyższy', 'liczba': 'mnoga', 'rodzaj': 'm'})))

    def testGetWordNoun(self):
        self.assertEqual(u'znak', self.ad.get_word(('rzeczownik', 'znak', {'przypadek': 'mianownik', 'liczba': 'pojedyncza'})))
        self.assertEqual(u'znaku', self.ad.get_word(('rzeczownik', 'znak', {'przypadek': 'dopełniacz', 'liczba': 'pojedyncza'})))
        self.assertEqual(u'znakowi', self.ad.get_word(('rzeczownik', 'znak', {'przypadek': 'celownik', 'liczba': 'pojedyncza'})))
        self.assertEqual(u'znak', self.ad.get_word(('rzeczownik', 'znak', {'przypadek': 'biernik', 'liczba': 'pojedyncza'})))
        self.assertEqual(u'znakiem', self.ad.get_word(('rzeczownik', 'znak', {'przypadek': 'narzędnik', 'liczba': 'pojedyncza'})))
        self.assertEqual(u'znaku', self.ad.get_word(('rzeczownik', 'znak', {'przypadek': 'miejscownik', 'liczba': 'pojedyncza'})))
        self.assertEqual(u'znaku', self.ad.get_word(('rzeczownik', 'znak', {'przypadek': 'wołacz', 'liczba': 'pojedyncza'})))
        
        self.assertEqual(u'znaki', self.ad.get_word(('rzeczownik', 'znak', {'przypadek': 'mianownik', 'liczba': 'mnoga'})))
        # self.assertEqual(u'znaków', self.ad.get_word(('rzeczownik', 'znak', {'przypadek': 'dopełniacz', 'liczba': 'mnoga'})))
        self.assertEqual(u'znakom', self.ad.get_word(('rzeczownik', 'znak', {'przypadek': 'celownik', 'liczba': 'mnoga'})))
        self.assertEqual(u'znaki', self.ad.get_word(('rzeczownik', 'znak', {'przypadek': 'biernik', 'liczba': 'mnoga'})))
        self.assertEqual(u'znakami', self.ad.get_word(('rzeczownik', 'znak', {'przypadek': 'narzędnik', 'liczba': 'mnoga'})))
        self.assertEqual(u'znakach', self.ad.get_word(('rzeczownik', 'znak', {'przypadek': 'miejscownik', 'liczba': 'mnoga'})))
        self.assertEqual(u'znaki', self.ad.get_word(('rzeczownik', 'znak', {'przypadek': 'wołacz', 'liczba': 'mnoga'})))
     

if __name__ == '__main__':
    #import sys;sys.argv = ['', 'Test.test']
    unittest.main()
