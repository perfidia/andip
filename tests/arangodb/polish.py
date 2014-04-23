# -*- coding: utf-8 -*-
import os
import unittest
from andip import FileProvider
from andip.arangodb import ArangoProvider

class GraphPolishTest(unittest.TestCase):
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

        cls.oracle = FileProvider(os.sep.join(path))
        data = eval(open("%s.txt" % os.sep.join(path)).read())
        provider =  ArangoProvider()
        provider.dropAll()
        provider.importData(data)
        provider.connect()
        cls.graph = provider

    
    def testGetWordPronoun(self):
        self.assertEqual(self.oracle.get_word(('zaimek', 'ja', {'przypadek': 'miejscownik', 'liczba': 'pojedyncza', 'osoba': 'trzecia', 'rodzaj': 'ż'})), self.graph.get_word(('zaimek', 'ja', {'przypadek': 'miejscownik', 'liczba': 'pojedyncza', 'osoba': 'trzecia', 'rodzaj': 'ż'})))
        self.assertEqual(self.oracle.get_word(('zaimek', 'ja', {'przypadek': 'miejscownik', 'liczba': 'pojedyncza', 'osoba': 'trzecia', 'rodzaj': 'm'})),  self.graph.get_word(('zaimek', 'ja', {'przypadek': 'miejscownik', 'liczba': 'pojedyncza', 'osoba': 'trzecia', 'rodzaj': 'm'})))
        self.assertEqual(self.oracle.get_word(('zaimek', 'ja', {'przypadek': 'miejscownik', 'liczba': 'mnoga', 'osoba': 'trzecia', 'rodzaj': 'm'})), self.graph.get_word(('zaimek', 'ja', {'przypadek': 'miejscownik', 'liczba': 'mnoga', 'osoba': 'trzecia', 'rodzaj': 'm'})))

        self.assertEqual(self.oracle.get_word(('zaimek', 'ja', {'przypadek': 'mianownik', 'liczba': 'pojedyncza', 'osoba': 'trzecia', 'rodzaj': 'm'})),   self.graph.get_word(('zaimek', 'ja', {'przypadek': 'mianownik', 'liczba': 'pojedyncza', 'osoba': 'trzecia', 'rodzaj': 'm'})))
        self.assertEqual(self.oracle.get_word(('zaimek', 'ja', {'przypadek': 'mianownik', 'liczba': 'pojedyncza', 'osoba': 'trzecia', 'rodzaj': 'ż'})),  self.graph.get_word(('zaimek', 'ja', {'przypadek': 'mianownik', 'liczba': 'pojedyncza', 'osoba': 'trzecia', 'rodzaj': 'ż'})))

        self.assertEqual(self.oracle.get_word(('zaimek', 'który', {'przypadek': 'miejscownik', 'liczba': 'pojedyncza', 'rodzaj': 'ż'})),  self.graph.get_word(('zaimek', 'który', {'przypadek': 'miejscownik', 'liczba': 'pojedyncza', 'rodzaj': 'ż'})))
        self.assertEqual(self.oracle.get_word(('zaimek', 'który', {'przypadek': 'miejscownik', 'liczba': 'pojedyncza', 'rodzaj': 'mos'})),  self.graph.get_word(('zaimek', 'który', {'przypadek': 'miejscownik', 'liczba': 'pojedyncza', 'rodzaj': 'mos'})))
        self.assertEqual(self.oracle.get_word(('zaimek', 'który', {'przypadek': 'miejscownik', 'liczba': 'mnoga', 'rodzaj': 'mos'})), self.graph.get_word(('zaimek', 'który', {'przypadek': 'miejscownik', 'liczba': 'mnoga', 'rodzaj': 'mos'})))

    def testGetWordVerb(self):
        self.assertEqual(self.oracle.get_word(('czasownik', 'następować', {'forma': 'czas teraźniejszy', 'liczba': 'pojedyncza', 'osoba': 'pierwsza'})), self.graph.get_word(('czasownik', 'następować', {'forma': 'czas teraźniejszy', 'liczba': 'pojedyncza', 'osoba': 'pierwsza'})))
        self.assertEqual(self.oracle.get_word(('czasownik', 'następować', {'forma': 'czas teraźniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'})), self.graph.get_word(('czasownik', 'następować', {'forma': 'czas teraźniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'})))

        self.assertEqual(self.oracle.get_word(('czasownik', 'występować', {'forma': 'czas teraźniejszy', 'liczba': 'pojedyncza', 'osoba': 'pierwsza'})), self.graph.get_word(('czasownik', 'występować', {'forma': 'czas teraźniejszy', 'liczba': 'pojedyncza', 'osoba': 'pierwsza'})))
        self.assertEqual(self.oracle.get_word(('czasownik', 'występować', {'forma': 'czas teraźniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'})), self.graph.get_word(('czasownik', 'występować', {'forma': 'czas teraźniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'})))

        self.assertEqual(self.oracle.get_word(('czasownik', 'być', {'forma': 'czas teraźniejszy', 'liczba': 'pojedyncza', 'osoba': 'trzecia'})), self.graph.get_word(('czasownik', 'być', {'forma': 'czas teraźniejszy', 'liczba': 'pojedyncza', 'osoba': 'trzecia'})))
        self.assertEqual(self.oracle.get_word(('czasownik', 'być', {'forma': 'czas teraźniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'})),   self.graph.get_word(('czasownik', 'być', {'forma': 'czas teraźniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'})))

    def testGetWordPreposition(self):
        self.assertEqual(self.oracle.get_word(('przyimek', 'z', {'forma': 'z'})),  self.graph.get_word(('przyimek', 'z', {'forma': 'z'})))
        self.assertEqual(self.oracle.get_word(('przyimek', 'z', {'forma': 'ze'})), self.graph.get_word(('przyimek', 'z', {'forma': 'ze'})))

    def testGetWordAdjective(self):
        self.assertEqual(self.oracle.get_word(('przymiotnik', 'opis', {'liczba': 'pojedyncza', 'rodzaj': 'm'})), self.graph.get_word(('przymiotnik', 'opis', {'liczba': 'pojedyncza', 'rodzaj': 'm'})))
        self.assertEqual(self.oracle.get_word(('przymiotnik', 'opis', {'liczba': 'mnoga', 'rodzaj': 'm'})), self.graph.get_word(('przymiotnik', 'opis', {'liczba': 'mnoga', 'rodzaj': 'm'})))
        self.assertEqual(self.oracle.get_word(('przymiotnik', 'opis', {'liczba': 'pojedyncza', 'rodzaj': 'ż'})), self.graph.get_word(('przymiotnik', 'opis', {'liczba': 'pojedyncza', 'rodzaj': 'ż'})))
        self.assertEqual(self.oracle.get_word(('przymiotnik', 'opis', {'liczba': 'mnoga', 'rodzaj': 'ż'})), self.graph.get_word(('przymiotnik', 'opis', {'liczba': 'mnoga', 'rodzaj': 'ż'})))

    def testGetWordNoun(self):
        self.assertEqual(self.oracle.get_word(('rzeczownik', 'znak', {'przypadek': 'dopełniacz', 'liczba': 'pojedyncza'})),  self.graph.get_word(('rzeczownik', 'znak', {'przypadek': 'dopełniacz', 'liczba': 'pojedyncza'})))
        self.assertEqual(self.oracle.get_word(('rzeczownik', 'znak', {'przypadek': 'dopełniacz', 'liczba': 'mnoga'})), self.graph.get_word(('rzeczownik', 'znak', {'przypadek': 'dopełniacz', 'liczba': 'mnoga'})))

    def testGetConfPronoun(self):
        self.assertIn(('zaimek', 'ja', {'przypadek': 'miejscownik', 'liczba': 'pojedyncza', 'osoba': 'trzecia', 'rodzaj': 'ż'}), self.graph.get_conf('niej'))
        self.assertIn(('zaimek', 'ja', {'przypadek': 'miejscownik', 'liczba': 'pojedyncza', 'osoba': 'trzecia', 'rodzaj': 'm'}),  self.graph.get_conf('nim'))
        self.assertIn(('zaimek', 'ja', {'przypadek': 'miejscownik', 'liczba': 'mnoga', 'osoba': 'trzecia', 'rodzaj': 'm'}), self.graph.get_conf('nich'))

        self.assertEqual(('zaimek', 'ja', {'przypadek': 'mianownik', 'liczba': 'pojedyncza', 'osoba': 'trzecia', 'rodzaj': 'm'}),  self.graph.get_conf('on')[0])
        self.assertEqual(('zaimek', 'ja', {'przypadek': 'mianownik', 'liczba': 'pojedyncza', 'osoba': 'trzecia', 'rodzaj': 'ż'}), self.graph.get_conf('ona')[0])

        self.assertIn(('zaimek', 'który', {'przypadek': 'miejscownik', 'liczba': 'pojedyncza', 'rodzaj': 'ż'}),  self.graph.get_conf('której'))
        self.assertIn(('zaimek', 'który', {'przypadek': 'miejscownik', 'liczba': 'pojedyncza', 'rodzaj': 'mos'}),  self.graph.get_conf('którym'))
        self.assertIn(('zaimek', 'który', {'przypadek': 'miejscownik', 'liczba': 'mnoga', 'rodzaj': 'mos'}), self.graph.get_conf('których'))

    def testGetConfVerb(self):
        self.assertIn(('czasownik', 'następować', {'forma': 'czas teraźniejszy', 'liczba': 'pojedyncza', 'osoba': 'pierwsza'}), self.graph.get_conf('następuje'))
        self.assertIn(('czasownik', 'następować', {'forma': 'czas teraźniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'}), self.graph.get_conf('następują'))

        self.assertIn(('czasownik', 'występować', {'forma': 'czas teraźniejszy', 'liczba': 'pojedyncza', 'osoba': 'pierwsza'}), self.graph.get_conf('występuje'))
        self.assertIn(('czasownik', 'występować', {'forma': 'czas teraźniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'}), self.graph.get_conf('występują'))

        self.assertIn(('czasownik', 'być', {'forma': 'czas teraźniejszy', 'liczba': 'pojedyncza', 'osoba': 'trzecia'}), self.graph.get_conf('jest'))
        self.assertIn(('czasownik', 'być', {'forma': 'czas teraźniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'}),   self.graph.get_conf('są'))

    def testGetConfPreposition(self):
        self.assertIn(('przyimek', 'z', {'forma': 'z'}),  self.graph.get_conf('z'))
        self.assertIn(('przyimek', 'z', {'forma': 'ze'}), self.graph.get_conf('ze'))

    def testGetConfAdjective(self):
        self.assertIn(('przymiotnik', 'opis', {'liczba': 'mnoga', 'rodzaj': 'm'}), self.graph.get_conf('opisane'))
        self.assertIn(('przymiotnik', 'opis', {'liczba': 'mnoga', 'rodzaj': 'ż'}), self.graph.get_conf('opisane'))

    def testGetConfNoun(self):
        self.assertIn(('rzeczownik', 'znak', {'przypadek': 'dopełniacz', 'liczba': 'pojedyncza'}),  self.graph.get_conf('znaku'))

        self.assertIn(('rzeczownik', 'znak', {'przypadek': 'mianownik', 'liczba': 'pojedyncza'}),  self.graph.get_conf('znak'))
        self.assertIn(('rzeczownik', 'znak', {'przypadek': 'mianownik', 'liczba': 'mnoga'}), self.graph.get_conf('znaki'))

if __name__ == '__main__':
    #import sys;sys.argv = ['', ''Test.test']
    unittest.main()
