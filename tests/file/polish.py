# -*- coding: utf-8 -*-
import os
import unittest
from andip import FileProvider

class FilePolishTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        path = os.getcwd().split(os.sep)

        for d in reversed(path[:]):
            if d != 'andip':
                path.pop()
                continue

            break

        path.append('data')
        path.append('polish')

        cls.ad = FileProvider(os.sep.join(path))

    def testGetWordPronoun(self):
        self.assertEqual('niej', self.ad.get_word(('zaimek', 'ja', {'przypadek': 'miejscownik', 'liczba': 'pojedyncza', 'osoba': 'trzecia', 'rodzaj': 'ż'})))
        self.assertEqual('nim',  self.ad.get_word(('zaimek', 'ja', {'przypadek': 'miejscownik', 'liczba': 'pojedyncza', 'osoba': 'trzecia', 'rodzaj': 'm'})))
        self.assertEqual('nich', self.ad.get_word(('zaimek', 'ja', {'przypadek': 'miejscownik', 'liczba': 'mnoga', 'osoba': 'trzecia', 'rodzaj': 'm'})))

        self.assertEqual('on',   self.ad.get_word(('zaimek', 'ja', {'przypadek': 'mianownik', 'liczba': 'pojedyncza', 'osoba': 'trzecia', 'rodzaj': 'm'})))
        self.assertEqual('ona',  self.ad.get_word(('zaimek', 'ja', {'przypadek': 'mianownik', 'liczba': 'pojedyncza', 'osoba': 'trzecia', 'rodzaj': 'ż'})))

        self.assertEqual('której',  self.ad.get_word(('zaimek', 'który', {'przypadek': 'miejscownik', 'liczba': 'pojedyncza', 'rodzaj': 'ż'})))
        self.assertEqual('którym',  self.ad.get_word(('zaimek', 'który', {'przypadek': 'miejscownik', 'liczba': 'pojedyncza', 'rodzaj': 'mos'})))
        self.assertEqual('których', self.ad.get_word(('zaimek', 'który', {'przypadek': 'miejscownik', 'liczba': 'mnoga', 'rodzaj': 'mos'})))

    def testGetWordVerb(self):
        self.assertEqual('następuje', self.ad.get_word(('czasownik', 'następować', {'aspekt': 'dokonane', 'forma': 'czas teraźniejszy', 'liczba': 'pojedyncza', 'osoba': 'pierwsza'})))
        self.assertEqual('następują', self.ad.get_word(('czasownik', 'następować', {'aspekt': 'dokonane', 'forma': 'czas teraźniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'})))

        self.assertEqual('występuje', self.ad.get_word(('czasownik', 'występować', {'aspekt': 'niedokonane', 'forma': 'czas teraźniejszy', 'liczba': 'pojedyncza', 'osoba': 'pierwsza'})))
        self.assertEqual('występują', self.ad.get_word(('czasownik', 'występować', {'aspekt': 'niedokonane', 'forma': 'czas teraźniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'})))

        self.assertEqual('jest', self.ad.get_word(('czasownik', 'być', {'aspekt': 'niedokonane', 'forma': 'czas teraźniejszy', 'liczba': 'pojedyncza', 'osoba': 'trzecia'})))
        self.assertEqual('są',   self.ad.get_word(('czasownik', 'być', {'aspekt': 'niedokonane', 'forma': 'czas teraźniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'})))

    def testGetWordPreposition(self):
        self.assertEqual('z',  self.ad.get_word(('przyimek', 'z', {'forma': 'z'})))
        self.assertEqual('ze', self.ad.get_word(('przyimek', 'z', {'forma': 'ze'})))

    def testGetWordAdjective(self):
        self.assertEqual('opisany', self.ad.get_word(('przymiotnik', 'opis', {'liczba': 'pojedyncza', 'rodzaj': 'm'})))
        self.assertEqual('opisane', self.ad.get_word(('przymiotnik', 'opis', {'liczba': 'mnoga', 'rodzaj': 'm'})))
        self.assertEqual('opisana', self.ad.get_word(('przymiotnik', 'opis', {'liczba': 'pojedyncza', 'rodzaj': 'ż'})))
        self.assertEqual('opisane', self.ad.get_word(('przymiotnik', 'opis', {'liczba': 'mnoga', 'rodzaj': 'ż'})))

    def testGetWordNoun(self):
        self.assertEqual('znaku',  self.ad.get_word(('rzeczownik', 'znak', {'przypadek': 'dopełniacz', 'liczba': 'pojedyncza'})))
        self.assertEqual('znaków', self.ad.get_word(('rzeczownik', 'znak', {'przypadek': 'dopełniacz', 'liczba': 'mnoga'})))

        self.assertEqual('znak',  self.ad.get_word(('rzeczownik', 'znak', {'przypadek': 'mianownik', 'liczba': 'pojedyncza'})))
        self.assertEqual('znaki', self.ad.get_word(('rzeczownik', 'znak', {'przypadek': 'mianownik', 'liczba': 'mnoga'})))

    def testGetConfPronoun(self):
        self.assertIn(('zaimek', 'ja', {'przypadek': 'miejscownik', 'liczba': 'pojedyncza', 'osoba': 'trzecia', 'rodzaj': 'ż'}), self.ad.get_conf('niej'))
        self.assertIn(('zaimek', 'ja', {'przypadek': 'miejscownik', 'liczba': 'pojedyncza', 'osoba': 'trzecia', 'rodzaj': 'm'}),  self.ad.get_conf('nim'))
        self.assertIn(('zaimek', 'ja', {'przypadek': 'miejscownik', 'liczba': 'mnoga', 'osoba': 'trzecia', 'rodzaj': 'm'}), self.ad.get_conf('nich'))

        self.assertEqual(('zaimek', 'ja', {'przypadek': 'mianownik', 'liczba': 'pojedyncza', 'osoba': 'trzecia', 'rodzaj': 'm'}),  self.ad.get_conf('on')[0])
        self.assertEqual(('zaimek', 'ja', {'przypadek': 'mianownik', 'liczba': 'pojedyncza', 'osoba': 'trzecia', 'rodzaj': 'ż'}), self.ad.get_conf('ona')[0])

        self.assertIn(('zaimek', 'który', {'przypadek': 'miejscownik', 'liczba': 'pojedyncza', 'rodzaj': 'ż'}),  self.ad.get_conf('której'))
        self.assertIn(('zaimek', 'który', {'przypadek': 'miejscownik', 'liczba': 'pojedyncza', 'rodzaj': 'mos'}),  self.ad.get_conf('którym'))
        self.assertIn(('zaimek', 'który', {'przypadek': 'miejscownik', 'liczba': 'mnoga', 'rodzaj': 'mos'}), self.ad.get_conf('których'))

    def testGetConfVerb(self):
        self.assertIn(('czasownik', 'następować', {'forma': 'czas teraźniejszy', 'liczba': 'pojedyncza', 'osoba': 'pierwsza'}), self.ad.get_conf('następuje'))
        self.assertEqual(('czasownik', 'następować', {'forma': 'czas teraźniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'}), self.ad.get_conf('następują')[0])

        self.assertIn(('czasownik', 'występować', {'forma': 'czas teraźniejszy', 'liczba': 'pojedyncza', 'osoba': 'pierwsza'}), self.ad.get_conf('występuje'))
        self.assertEqual(('czasownik', 'występować', {'forma': 'czas teraźniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'}), self.ad.get_conf('występują')[0])

        self.assertEqual(('czasownik', 'być', {'forma': 'czas teraźniejszy', 'liczba': 'pojedyncza', 'osoba': 'trzecia'}), self.ad.get_conf('jest')[0])
        self.assertEqual(('czasownik', 'być', {'forma': 'czas teraźniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'}),   self.ad.get_conf('są')[0])

    def testGetConfPreposition(self):
        self.assertEqual(('przyimek', 'z', {'forma': 'z'}),  self.ad.get_conf('z')[0])
        self.assertEqual(('przyimek', 'z', {'forma': 'ze'}), self.ad.get_conf('ze')[0])

    def testGetConfAdjective(self):
        self.assertEqual(('przymiotnik', 'opis', {'liczba': 'pojedyncza', 'rodzaj': 'm'}), self.ad.get_conf('opisany')[0])
        self.assertIn(('przymiotnik', 'opis', {'liczba': 'mnoga', 'rodzaj': 'm'}), self.ad.get_conf('opisane'))
        self.assertEqual(('przymiotnik', 'opis', {'liczba': 'pojedyncza', 'rodzaj': 'ż'}), self.ad.get_conf('opisana')[0])
        self.assertIn(('przymiotnik', 'opis', {'liczba': 'mnoga', 'rodzaj': 'ż'}), self.ad.get_conf('opisane'))

    def testGetConfNoun(self):
        self.assertIn(('rzeczownik', 'znak', {'przypadek': 'dopełniacz', 'liczba': 'pojedyncza'}),  self.ad.get_conf('znaku'))
        self.assertEqual(('rzeczownik', 'znak', {'przypadek': 'dopełniacz', 'liczba': 'mnoga'}), self.ad.get_conf('znaków')[0])

        self.assertIn(('rzeczownik', 'znak', {'przypadek': 'mianownik', 'liczba': 'pojedyncza'}),  self.ad.get_conf('znak'))
        self.assertIn(('rzeczownik', 'znak', {'przypadek': 'mianownik', 'liczba': 'mnoga'}), self.ad.get_conf('znaki'))

if __name__ == '__main__':
    #import sys;sys.argv = ['', ''Test.test']
    unittest.main()
