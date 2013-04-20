# -*- coding: utf-8 -*-
import os
import unittest
from andip import AnDiP
from andip.provider import FileProvider

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

		cls.ad = AnDiP(FileProvider(os.sep.join(path)))

	def testGetWordPronoun(self):
		self.assertEqual(u'niej', self.ad.get_word(('zaimek', 'ja', {'przypadek': 'miejscownik', 'liczba': 'pojedyncza', 'osoba': 'trzecia', 'rodzaj': 'ż'})))
		self.assertEqual(u'nim',  self.ad.get_word(('zaimek', 'ja', {'przypadek': 'miejscownik', 'liczba': 'pojedyncza', 'osoba': 'trzecia', 'rodzaj': 'm'})))
		self.assertEqual(u'nich', self.ad.get_word(('zaimek', 'ja', {'przypadek': 'miejscownik', 'liczba': 'mnoga', 'osoba': 'trzecia', 'rodzaj': 'm'})))

		self.assertEqual(u'on',   self.ad.get_word(('zaimek', 'ja', {'przypadek': 'mianownik', 'liczba': 'pojedyncza', 'osoba': 'trzecia', 'rodzaj': 'm'})))
		self.assertEqual(u'ona',  self.ad.get_word(('zaimek', 'ja', {'przypadek': 'mianownik', 'liczba': 'pojedyncza', 'osoba': 'trzecia', 'rodzaj': 'ż'})))

		self.assertEqual(u'której',  self.ad.get_word(('zaimek', 'który', {'przypadek': 'miejscownik', 'liczba': 'pojedyncza', 'rodzaj': 'ż'})))
		self.assertEqual(u'którym',  self.ad.get_word(('zaimek', 'który', {'przypadek': 'miejscownik', 'liczba': 'pojedyncza', 'rodzaj': 'mos'})))
		self.assertEqual(u'których', self.ad.get_word(('zaimek', 'który', {'przypadek': 'miejscownik', 'liczba': 'mnoga', 'rodzaj': 'mos'})))

	def testGetWordVerb(self):
		self.assertEqual(u'następuje', self.ad.get_word(('czasownik', 'następować', {'aspekt': 'dokonane', 'forma': 'czas teraźniejszy', 'liczba': 'pojedyncza', 'osoba': 'pierwsza'})))
		self.assertEqual(u'następują', self.ad.get_word(('czasownik', 'następować', {'aspekt': 'dokonane', 'forma': 'czas teraźniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'})))

		self.assertEqual(u'występuje', self.ad.get_word(('czasownik', 'występować', {'aspekt': 'dokonane', 'forma': 'czas teraźniejszy', 'liczba': 'pojedyncza', 'osoba': 'pierwsza'})))
		self.assertEqual(u'występują', self.ad.get_word(('czasownik', 'występować', {'aspekt': 'dokonane', 'forma': 'czas teraźniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'})))

		self.assertEqual(u'jest', self.ad.get_word(('czasownik', 'być', {'aspekt': 'dokonane', 'forma': 'czas teraźniejszy', 'liczba': 'pojedyncza', 'osoba': 'trzecia'})))
		self.assertEqual(u'są',   self.ad.get_word(('czasownik', 'być', {'aspekt': 'dokonane', 'forma': 'czas teraźniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'})))

	def testGetWordPreposition(self):
		self.assertEqual(u'z',  self.ad.get_word(('przyimek', 'z', {'forma': 'z'})))
		self.assertEqual(u'ze', self.ad.get_word(('przyimek', 'z', {'forma': 'ze'})))

	def testGetWordAdjective(self):
		self.assertEqual(u'opisany', self.ad.get_word(('przymiotnik', 'opis', {'liczba': 'pojedyncza', 'rodzaj': 'm'})))
		self.assertEqual(u'opisane', self.ad.get_word(('przymiotnik', 'opis', {'liczba': 'mnoga', 'rodzaj': 'm'})))
		self.assertEqual(u'opisana', self.ad.get_word(('przymiotnik', 'opis', {'liczba': 'pojedyncza', 'rodzaj': 'ż'})))
		self.assertEqual(u'opisane', self.ad.get_word(('przymiotnik', 'opis', {'liczba': 'mnoga', 'rodzaj': 'ż'})))

	def testGetWordNoun(self):
		self.assertEqual(u'znaku',  self.ad.get_word(('rzeczownik', 'znak', {'przypadek': 'dopełniacz', 'liczba': 'pojedyncza'})))
		self.assertEqual(u'znaków', self.ad.get_word(('rzeczownik', 'znak', {'przypadek': 'dopełniacz', 'liczba': 'mnoga'})))

		self.assertEqual(u'znak',  self.ad.get_word(('rzeczownik', 'znak', {'przypadek': 'mianownik', 'liczba': 'pojedyncza'})))
		self.assertEqual(u'znaki', self.ad.get_word(('rzeczownik', 'znak', {'przypadek': 'mianownik', 'liczba': 'mnoga'})))

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
		self.assertIn(('czasownik', 'następować', {'aspekt': 'dokonane', 'forma': 'czas teraźniejszy', 'liczba': 'pojedyncza', 'osoba': 'pierwsza'}), self.ad.get_conf('następuje'))
		self.assertEqual(('czasownik', 'następować', {'aspekt': 'dokonane', 'forma': 'czas teraźniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'}), self.ad.get_conf('następują')[0])

		self.assertIn(('czasownik', 'występować', {'aspekt': 'dokonane', 'forma': 'czas teraźniejszy', 'liczba': 'pojedyncza', 'osoba': 'pierwsza'}), self.ad.get_conf('występuje'))
		self.assertEqual(('czasownik', 'występować', {'aspekt': 'dokonane', 'forma': 'czas teraźniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'}), self.ad.get_conf('występują')[0])

		self.assertEqual(('czasownik', 'być', {'aspekt': 'dokonane', 'forma': 'czas teraźniejszy', 'liczba': 'pojedyncza', 'osoba': 'trzecia'}), self.ad.get_conf('jest')[0])
		self.assertEqual(('czasownik', 'być', {'aspekt': 'dokonane', 'forma': 'czas teraźniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'}),   self.ad.get_conf('są')[0])

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
