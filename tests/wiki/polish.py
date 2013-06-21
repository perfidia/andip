# -*- coding: utf-8 -*-
import unittest
from andip import PlWikiProvider

class WikiPolishTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ad = PlWikiProvider()

    def testGetWordVerb(self):
        self.assertEquals('występują',    self.ad.get_word(('czasownik', 'występować', {'aspekt' : 'niedokonane', 'forma' : 'czas teraźniejszy', 'liczba' : 'mnoga', 'osoba': 'trzecia'})))
        self.assertEquals('występuje',    self.ad.get_word(('czasownik', 'występować', {'aspekt' : 'niedokonane', 'forma' : 'czas teraźniejszy', 'liczba' : 'pojedyncza', 'osoba': 'trzecia'})))
        self.assertEquals('występujemy',  self.ad.get_word(('czasownik', 'występować', {'aspekt' : 'niedokonane', 'forma' : 'czas teraźniejszy', 'liczba' : 'mnoga', 'osoba': 'pierwsza'})))
        self.assertEquals('występujecie', self.ad.get_word(('czasownik', 'występować', {'aspekt' : 'niedokonane', 'forma' : 'czas teraźniejszy', 'liczba' : 'mnoga', 'osoba': 'druga'})))
        self.assertEquals('występujesz',  self.ad.get_word(('czasownik', 'występować', {'aspekt' : 'niedokonane', 'forma' : 'czas teraźniejszy', 'liczba' : 'pojedyncza', 'osoba': 'druga'})))

        self.assertEqual(u'jest', self.ad.get_word(('czasownik', 'być', {'aspekt' : 'niedokonane', 'forma': 'czas teraźniejszy', 'liczba': 'pojedyncza', 'osoba': 'trzecia'})))
        # self.assertEqual(u'są',   self.ad.get_word(('czasownik', 'być', {'aspekt': 'niedokonane', 'forma': 'czas teraźniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'})))

    def testGetWordVerbIrregularByc(self):
        # source: http://pl.wiktionary.org/wiki/by%C4%87

        # czas teraźniejszy

        forma = 'czas teraźniejszy'

        self.assertEqual('jestem',      self.ad.get_word(('czasownik', 'być', {'aspekt' : 'niedokonane', 'forma': forma, 'liczba': 'pojedyncza', 'osoba': 'pierwsza'})))
        self.assertEqual('jesteś',      self.ad.get_word(('czasownik', 'być', {'aspekt' : 'niedokonane', 'forma': forma, 'liczba': 'pojedyncza', 'osoba': 'druga'})))
        self.assertEqual('jest',        self.ad.get_word(('czasownik', 'być', {'aspekt' : 'niedokonane', 'forma': forma, 'liczba': 'pojedyncza', 'osoba': 'trzecia'})))
        self.assertEqual('jesteśmy',    self.ad.get_word(('czasownik', 'być', {'aspekt' : 'niedokonane', 'forma': forma, 'liczba': 'mnoga',      'osoba': 'pierwsza'})))
        self.assertEqual('jesteście',   self.ad.get_word(('czasownik', 'być', {'aspekt' : 'niedokonane', 'forma': forma, 'liczba': 'mnoga',      'osoba': 'druga'})))
        self.assertEqual('są',          self.ad.get_word(('czasownik', 'być', {'aspekt' : 'niedokonane', 'forma': forma, 'liczba': 'mnoga',      'osoba': 'trzecia'})))

        # czas przeszły

        forma = 'czas przeszły'

        self.assertEqual('byłem',       self.ad.get_word(('czasownik', 'być', {'aspekt' : 'niedokonane', 'forma': forma, 'liczba': 'pojedyncza',     'osoba': 'pierwsza', 'rodzaj': 'm'})))
        # self.assertEqual('byłeś',       self.ad.get_word(('czasownik', 'być', {'aspekt' : 'niedokonane', 'forma': forma, 'liczba': 'pojedyncza',     'osoba': 'druga',    'rodzaj': 'm'})))
        self.assertEqual('był',         self.ad.get_word(('czasownik', 'być', {'aspekt' : 'niedokonane', 'forma': forma, 'liczba': 'pojedyncza',     'osoba': 'trzecia',  'rodzaj': 'm'})))
        # self.assertEqual('bylismy',     self.ad.get_word(('czasownik', 'być', {'aspekt' : 'niedokonane', 'forma': forma, 'liczba': 'mnoga',          'osoba': 'pierwsza', 'rodzaj': 'm'})))
        # self.assertEqual('byliście',    self.ad.get_word(('czasownik', 'być', {'aspekt' : 'niedokonane', 'forma': forma, 'liczba': 'mnoga',          'osoba': 'druga',    'rodzaj': 'm'})))
        self.assertEqual('byli',        self.ad.get_word(('czasownik', 'być', {'aspekt' : 'niedokonane', 'forma': forma, 'liczba': 'mnoga',	         'osoba': 'trzecia',  'rodzaj': 'm'})))

        # self.assertEqual('byłam',       self.ad.get_word(('czasownik', 'być', {'aspekt' : 'niedokonane', 'forma': forma, 'liczba': 'pojedyncza',     'osoba': 'pierwsza', 'rodzaj': 'ż'})))
        # self.assertEqual('byłaś',       self.ad.get_word(('czasownik', 'być', {'aspekt' : 'niedokonane', 'forma': forma, 'liczba': 'pojedyncza',     'osoba': 'druga',    'rodzaj': 'ż'})))
        self.assertEqual('była',        self.ad.get_word(('czasownik', 'być', {'aspekt' : 'niedokonane', 'forma': forma, 'liczba': 'pojedyncza',     'osoba': 'trzecia',  'rodzaj': 'ż'})))
        # self.assertEqual('byłyśmy',     self.ad.get_word(('czasownik', 'być', {'aspekt' : 'niedokonane', 'forma': forma, 'liczba': 'mnoga',          'osoba': 'pierwsza', 'rodzaj': 'ż'})))
        # self.assertEqual('byłyście',    self.ad.get_word(('czasownik', 'być', {'aspekt' : 'niedokonane', 'forma': forma, 'liczba': 'mnoga',          'osoba': 'druga',    'rodzaj': 'ż'})))
        # self.assertEqual('były',        self.ad.get_word(('czasownik', 'być', {'aspekt' : 'niedokonane', 'forma': forma, 'liczba': 'mnoga',          'osoba': 'trzecia',  'rodzaj': 'ż'})))

        # self.assertEqual('byłom',       self.ad.get_word(('czasownik', 'być', {'aspekt' : 'niedokonane', 'forma': forma, 'liczba': 'pojedyncza',     'osoba': 'pierwsza', 'rodzaj': 'n'})))
        # self.assertEqual('byłoś',       self.ad.get_word(('czasownik', 'być', {'aspekt' : 'niedokonane', 'forma': forma, 'liczba': 'pojedyncza',     'osoba': 'druga',    'rodzaj': 'n'})))
        # self.assertEqual('było',        self.ad.get_word(('czasownik', 'być', {'aspekt' : 'niedokonane', 'forma': forma, 'liczba': 'pojedyncza',     'osoba': 'trzecia',  'rodzaj': 'n'})))
        # self.assertEqual('byłyśmy',     self.ad.get_word(('czasownik', 'być', {'aspekt' : 'niedokonane', 'forma': forma, 'liczba': 'mnoga',          'osoba': 'pierwsza', 'rodzaj': 'n'})))
        # self.assertEqual('byłyście',    self.ad.get_word(('czasownik', 'być', {'aspekt' : 'niedokonane', 'forma': forma, 'liczba': 'mnoga',          'osoba': 'druga',    'rodzaj': 'n'})))
        # self.assertEqual('były',        self.ad.get_word(('czasownik', 'być', {'aspekt' : 'niedokonane', 'forma': forma, 'liczba': 'mnoga',          'osoba': 'trzecia',  'rodzaj': 'n'})))

        # czas przyszły

        forma = 'czas przyszły'

        self.assertEqual('będę',         self.ad.get_word(('czasownik', 'być', {'aspekt' : 'niedokonane', 'forma': forma, 'liczba': 'pojedyncza',     'osoba': 'pierwsza', 'rodzaj': 'm'})))
        self.assertEqual('będziesz',     self.ad.get_word(('czasownik', 'być', {'aspekt' : 'niedokonane', 'forma': forma, 'liczba': 'pojedyncza',     'osoba': 'druga',    'rodzaj': 'm'})))
        self.assertEqual('będzie',       self.ad.get_word(('czasownik', 'być', {'aspekt' : 'niedokonane', 'forma': forma, 'liczba': 'pojedyncza',     'osoba': 'trzecia',  'rodzaj': 'm'})))
        self.assertEqual('będziemy',     self.ad.get_word(('czasownik', 'być', {'aspekt' : 'niedokonane', 'forma': forma, 'liczba': 'mnoga',          'osoba': 'pierwsza', 'rodzaj': 'm'})))
        self.assertEqual('będziecie',    self.ad.get_word(('czasownik', 'być', {'aspekt' : 'niedokonane', 'forma': forma, 'liczba': 'mnoga',          'osoba': 'druga',    'rodzaj': 'm'})))
        self.assertEqual('będą',         self.ad.get_word(('czasownik', 'być', {'aspekt' : 'niedokonane', 'forma': forma, 'liczba': 'mnoga',          'osoba': 'trzecia',  'rodzaj': 'm'})))

        self.assertEqual('będę',         self.ad.get_word(('czasownik', 'być', {'aspekt' : 'niedokonane', 'forma': forma, 'liczba': 'pojedyncza',     'osoba': 'pierwsza', 'rodzaj': 'ż'})))
        self.assertEqual('będziesz',     self.ad.get_word(('czasownik', 'być', {'aspekt' : 'niedokonane', 'forma': forma, 'liczba': 'pojedyncza',     'osoba': 'druga',    'rodzaj': 'ż'})))
        self.assertEqual('będzie',       self.ad.get_word(('czasownik', 'być', {'aspekt' : 'niedokonane', 'forma': forma, 'liczba': 'pojedyncza',     'osoba': 'trzecia',  'rodzaj': 'ż'})))
        self.assertEqual('będziemy',     self.ad.get_word(('czasownik', 'być', {'aspekt' : 'niedokonane', 'forma': forma, 'liczba': 'mnoga',          'osoba': 'pierwsza', 'rodzaj': 'ż'})))
        self.assertEqual('będziecie',    self.ad.get_word(('czasownik', 'być', {'aspekt' : 'niedokonane', 'forma': forma, 'liczba': 'mnoga',          'osoba': 'druga',    'rodzaj': 'ż'})))
        self.assertEqual('będą',         self.ad.get_word(('czasownik', 'być', {'aspekt' : 'niedokonane', 'forma': forma, 'liczba': 'mnoga',          'osoba': 'trzecia',  'rodzaj': 'ż'})))

        self.assertEqual('będę',         self.ad.get_word(('czasownik', 'być', {'aspekt' : 'niedokonane', 'forma': forma, 'liczba': 'pojedyncza',     'osoba': 'pierwsza', 'rodzaj': 'n'})))
        self.assertEqual('będziesz',     self.ad.get_word(('czasownik', 'być', {'aspekt' : 'niedokonane', 'forma': forma, 'liczba': 'pojedyncza',     'osoba': 'druga',    'rodzaj': 'n'})))
        self.assertEqual('będzie',       self.ad.get_word(('czasownik', 'być', {'aspekt' : 'niedokonane', 'forma': forma, 'liczba': 'pojedyncza',     'osoba': 'trzecia',  'rodzaj': 'n'})))
        self.assertEqual('będziemy',     self.ad.get_word(('czasownik', 'być', {'aspekt' : 'niedokonane', 'forma': forma, 'liczba': 'mnoga',          'osoba': 'pierwsza', 'rodzaj': 'n'})))
        self.assertEqual('będziecie',    self.ad.get_word(('czasownik', 'być', {'aspekt' : 'niedokonane', 'forma': forma, 'liczba': 'mnoga',          'osoba': 'druga',    'rodzaj': 'n'})))
        self.assertEqual('będą',         self.ad.get_word(('czasownik', 'być', {'aspekt' : 'niedokonane', 'forma': forma, 'liczba': 'mnoga',          'osoba': 'trzecia',  'rodzaj': 'n'})))


    def testGetWordAdjective(self):
        self.assertEquals('zachodnich',  self.ad.get_word(('przymiotnik', 'zachodni', {'stopień': 'podstawowy', 'przypadek' : 'dopełniacz', 'liczba': 'mnoga', 'rodzaj': 'm'})))
        self.assertEquals('zachodniego', self.ad.get_word(('przymiotnik', 'zachodni', {'stopień': 'podstawowy', 'przypadek' : 'biernik', 'liczba': 'pojedyncza', 'rodzaj': 'm'})))
        self.assertEquals('zachodniego', self.ad.get_word(('przymiotnik', 'zachodni', {'stopień': 'podstawowy', 'przypadek' : 'dopełniacz', 'liczba': 'pojedyncza', 'rodzaj': 'm'})))
        self.assertEquals('zachodnim',   self.ad.get_word(('przymiotnik', 'zachodni', {'stopień': 'podstawowy', 'przypadek' : 'miejscownik', 'liczba': 'pojedyncza', 'rodzaj': 'm'})))
        self.assertEquals('zachodniej',  self.ad.get_word(('przymiotnik', 'zachodni', {'stopień': 'podstawowy', 'przypadek' : 'miejscownik', 'liczba': 'pojedyncza', 'rodzaj': 'ż'})))

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

    def testGetConfVerb(self):
        # download and save in buffer
        self.assertEqual('robią', self.ad.get_word(("czasownik", "robić",
                            {'aspekt': 'niedokonane', 'forma': 'czas teraźniejszy', 'liczba': 'mnoga',
                             'osoba': 'trzecia'})))
        self.assertEqual('występował', self.ad.get_word(("czasownik", "występować",
                            {'aspekt': 'niedokonane', 'forma': 'czas przeszły', 'liczba': 'pojedyncza',
                             'osoba': 'trzecia', 'rodzaj': 'm'})))

        # test
        self.assertEqual(self.ad.get_conf('robiłem'), [('czasownik', 'robi\xc4\x87', {'rodzaj': 'm', 'forma': 'czas przesz\xc5\x82y', 'osoba': 'pierwsza', 'aspekt': 'niedokonane', 'liczba': 'pojedyncza'})])
        self.assertEqual(self.ad.get_conf('robię'), [('czasownik', 'robi\xc4\x87', {'forma': 'czas tera\xc5\xbaniejszy', 'osoba': 'pierwsza', 'aspekt': 'niedokonane', 'liczba': 'pojedyncza'})])
        self.assertEqual(self.ad.get_conf('robili'), [('czasownik', 'robi\xc4\x87', {'rodzaj': 'm', 'forma': 'czas przesz\xc5\x82y', 'osoba': 'trzecia', 'aspekt': 'niedokonane', 'liczba': 'mnoga'})])
        self.assertEqual(self.ad.get_conf('występowałam'), [('czasownik', 'wyst\xc4\x99powa\xc4\x87', {'rodzaj': '\xc5\xbc', 'forma': 'czas przesz\xc5\x82y', 'osoba': 'pierwsza', 'aspekt': 'niedokonane', 'liczba': 'pojedyncza'})])
        self.assertEqual(self.ad.get_conf('występują'), [('czasownik', 'wyst\xc4\x99powa\xc4\x87', {'forma': 'czas tera\xc5\xbaniejszy', 'osoba': 'trzecia', 'aspekt': 'niedokonane', 'liczba': 'mnoga'})])

if __name__ == '__main__':
    #import sys;sys.argv = ['', 'Test.test']
    unittest.main()
