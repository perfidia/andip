# -*- coding: utf-8 -*-
import unittest
from andip import PlWikiProvider

class WikiPolishTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ad = PlWikiProvider()

    def testGetWordVerb(self):
        self.assertEquals('występują',    self.ad.get_word(('czasownik', 'występować', {'aspekt' : 'niedokonane', 'forma' : 'czas teraźniejszy', 'liczba' : 'mnoga', 'osoba': 'trzecia'})))
        self.assertEquals('występuje',    self.ad.get_word(('czasownik', 'występować', {'aspekt' : 'niedokonane', 'forma' : 'czas teraźniejszy', 'liczba' : 'pojedyńcza', 'osoba': 'trzecia'})))
        self.assertEquals('występujemy',  self.ad.get_word(('czasownik', 'występować', {'aspekt' : 'niedokonane', 'forma' : 'czas teraźniejszy', 'liczba' : 'mnoga', 'osoba': 'pierwsza'})))
        self.assertEquals('występujecie', self.ad.get_word(('czasownik', 'występować', {'aspekt' : 'niedokonane', 'forma' : 'czas teraźniejszy', 'liczba' : 'mnoga', 'osoba': 'druga'})))
        self.assertEquals('występujesz',  self.ad.get_word(('czasownik', 'występować', {'aspekt' : 'niedokonane', 'forma' : 'czas teraźniejszy', 'liczba' : 'pojedyńcza', 'osoba': 'druga'})))

        self.assertEqual(u'jest', self.ad.get_word(('czasownik', 'być', {'aspekt' : 'niedokonane', 'forma': 'czas teraźniejszy', 'liczba': 'pojedyńcza', 'osoba': 'trzecia'})))
        # self.assertEqual(u'są',   self.ad.get_word(('czasownik', 'być', {'aspekt': 'niedokonane', 'forma': 'czas teraźniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'})))

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
        self.assertEqual(u'znak', self.ad.get_word(('rzeczownik', 'znak', {'przypadek': 'mianownik', 'liczba': 'pojedyńcza'})))
        self.assertEqual(u'znaku', self.ad.get_word(('rzeczownik', 'znak', {'przypadek': 'dopełniacz', 'liczba': 'pojedyńcza'})))
        self.assertEqual(u'znakowi', self.ad.get_word(('rzeczownik', 'znak', {'przypadek': 'celownik', 'liczba': 'pojedyńcza'})))
        self.assertEqual(u'znak', self.ad.get_word(('rzeczownik', 'znak', {'przypadek': 'biernik', 'liczba': 'pojedyńcza'})))
        self.assertEqual(u'znakiem', self.ad.get_word(('rzeczownik', 'znak', {'przypadek': 'narzędnik', 'liczba': 'pojedyńcza'})))
        self.assertEqual(u'znaku', self.ad.get_word(('rzeczownik', 'znak', {'przypadek': 'miejscownik', 'liczba': 'pojedyńcza'})))
        self.assertEqual(u'znaku', self.ad.get_word(('rzeczownik', 'znak', {'przypadek': 'wołacz', 'liczba': 'pojedyńcza'})))
        
        self.assertEqual(u'znaki', self.ad.get_word(('rzeczownik', 'znak', {'przypadek': 'mianownik', 'liczba': 'mnoga'})))
        # self.assertEqual(u'znaków', self.ad.get_word(('rzeczownik', 'znak', {'przypadek': 'dopełniacz', 'liczba': 'mnoga'})))
        self.assertEqual(u'znakom', self.ad.get_word(('rzeczownik', 'znak', {'przypadek': 'celownik', 'liczba': 'mnoga'})))
        self.assertEqual(u'znaki', self.ad.get_word(('rzeczownik', 'znak', {'przypadek': 'biernik', 'liczba': 'mnoga'})))
        self.assertEqual(u'znakami', self.ad.get_word(('rzeczownik', 'znak', {'przypadek': 'narzędnik', 'liczba': 'mnoga'})))
        self.assertEqual(u'znakach', self.ad.get_word(('rzeczownik', 'znak', {'przypadek': 'miejscownik', 'liczba': 'mnoga'})))
        self.assertEqual(u'znaki', self.ad.get_word(('rzeczownik', 'znak', {'przypadek': 'wołacz', 'liczba': 'mnoga'})))
     
    def testGetConfVerb(self):
        # download and save in buffer
        self.assertEqual('robią', self.ad.get_word(("czasownik", "robić",
                            {'aspekt': 'niedokonane', 'forma': 'czas teraźniejszy', 'liczba': 'mnoga',
                             'osoba': 'trzecia'})))
        self.assertEqual('występował', self.ad.get_word(("czasownik", "występować",
                            {'aspekt': 'niedokonane', 'forma': 'czas przeszły', 'liczba': 'pojedyńcza',
                             'osoba': 'trzecia', 'rodzaj': 'm'})))

        # test
        self.assertEqual(self.ad.get_conf('robiłem'), [('czasownik', 'robi\xc4\x87', {'rodzaj': 'm', 'forma': 'czas przesz\xc5\x82y', 'osoba': 'pierwsza', 'aspekt': 'niedokonane', 'liczba': 'pojedy\xc5\x84cza'})])
        self.assertEqual(self.ad.get_conf('robię'), [('czasownik', 'robi\xc4\x87', {'forma': 'czas tera\xc5\xbaniejszy', 'osoba': 'pierwsza', 'aspekt': 'niedokonane', 'liczba': 'pojedy\xc5\x84cza'})])
        self.assertEqual(self.ad.get_conf('robili'), [('czasownik', 'robi\xc4\x87', {'rodzaj': 'm', 'forma': 'czas przesz\xc5\x82y', 'osoba': 'trzecia', 'aspekt': 'niedokonane', 'liczba': 'mnoga'})])
        self.assertEqual(self.ad.get_conf('występowałam'), [('czasownik', 'wyst\xc4\x99powa\xc4\x87', {'rodzaj': '\xc5\xbc', 'forma': 'czas przesz\xc5\x82y', 'osoba': 'pierwsza', 'aspekt': 'niedokonane', 'liczba': 'pojedy\xc5\x84cza'})])
        self.assertEqual(self.ad.get_conf('występują'), [('czasownik', 'wyst\xc4\x99powa\xc4\x87', {'forma': 'czas tera\xc5\xbaniejszy', 'osoba': 'trzecia', 'aspekt': 'niedokonane', 'liczba': 'mnoga'})])

if __name__ == '__main__':
    #import sys;sys.argv = ['', 'Test.test']
    unittest.main()
