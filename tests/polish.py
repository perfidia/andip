# -*- coding: utf-8 -*-

import unittest
from andip import AnDiP
from andip.provider import FileProvider

class PolishTest(unittest.TestCase):
	def setUp(self):
		self.ad = AnDiP(FileProvider('../data/polish'))

	def testGetWordPronoun(self):
		self.assertEqual(u'niej', self.ad.get_word(('zaimek', 'ja', {'przypadek': 'miejscownik', 'liczba': 'pojedyncza', 'osoba': 'trzecia', 'rodzaj': 'ĹĽ'})))
		self.assertEqual(u'nim',  self.ad.get_word(('zaimek', 'ja', {'przypadek': 'miejscownik', 'liczba': 'pojedyncza', 'osoba': 'trzecia', 'rodzaj': 'm'})))
		self.assertEqual(u'nich', self.ad.get_word(('zaimek', 'ja', {'przypadek': 'miejscownik', 'liczba': 'mnoga', 'osoba': 'trzecia', 'rodzaj': 'm'})))

		self.assertEqual(u'on',   self.ad.get_word(('zaimek', 'ja', {'przypadek': 'mianownik', 'liczba': 'pojedyncza', 'osoba': 'trzecia', 'rodzaj': 'm'})))
		self.assertEqual(u'ona', self.ad.get_word(('zaimek', 'ja', {'przypadek': 'mianownik', 'liczba': 'pojedyncza', 'osoba': 'trzecia', 'rodzaj': 'ĹĽ'})))

		self.assertEqual(u'ktĂłrej',  self.ad.get_word(('zaimek', 'ktĂłry', {'przypadek': 'miejscownik', 'liczba': 'pojedyncza', 'rodzaj': 'ĹĽ'})))
		self.assertEqual(u'ktĂłrym',  self.ad.get_word(('zaimek', 'ktĂłry', {'przypadek': 'miejscownik', 'liczba': 'pojedyncza', 'rodzaj': 'mos'})))
		self.assertEqual(u'ktĂłrych', self.ad.get_word(('zaimek', 'ktĂłry', {'przypadek': 'miejscownik', 'liczba': 'mnoga', 'rodzaj': 'mos'})))

	def testGetWordVerb(self):
		self.assertEqual(u'nastÄ™puje', self.ad.get_word(('czasownik', 'nastÄ™powaÄ‡', {'aspekt': 'dokonane', 'forma': 'czas teraĹşniejszy', 'liczba': 'pojedyncza', 'osoba': 'pierwsza'})))
		self.assertEqual(u'nastÄ™pujÄ…', self.ad.get_word(('czasownik', 'nastÄ™powaÄ‡', {'aspekt': 'dokonane', 'forma': 'czas teraĹşniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'})))

		self.assertEqual(u'wystÄ™puje', self.ad.get_word(('czasownik', 'wystÄ™powaÄ‡', {'aspekt': 'dokonane', 'forma': 'czas teraĹşniejszy', 'liczba': 'pojedyncza', 'osoba': 'pierwsza'})))
		self.assertEqual(u'wystÄ™pujÄ…', self.ad.get_word(('czasownik', 'wystÄ™powaÄ‡', {'aspekt': 'dokonane', 'forma': 'czas teraĹşniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'})))

		self.assertEqual(u'jest', self.ad.get_word(('czasownik', 'byÄ‡', {'aspekt': 'dokonane', 'forma': 'czas teraĹşniejszy', 'liczba': 'pojedyncza', 'osoba': 'trzecia'})))
		self.assertEqual(u'sÄ…',   self.ad.get_word(('czasownik', 'byÄ‡', {'aspekt': 'dokonane', 'forma': 'czas teraĹşniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'})))

	def testGetWordPreposition(self):
		self.assertEqual(u'z',  self.ad.get_word(('przyimek', 'z', {'forma': 'z'})))
		self.assertEqual(u'ze', self.ad.get_word(('przyimek', 'z', {'forma': 'ze'})))

	def testGetWordAdjective(self):
		self.assertEqual(u'opisany', self.ad.get_word(('przymiotnik', 'opis', {'liczba': 'pojedyncza', 'rodzaj': 'm'})))
		self.assertEqual(u'opisane', self.ad.get_word(('przymiotnik', 'opis', {'liczba': 'mnoga', 'rodzaj': 'm'})))
		self.assertEqual(u'opisana', self.ad.get_word(('przymiotnik', 'opis', {'liczba': 'pojedyncza', 'rodzaj': 'ĹĽ'})))
		self.assertEqual(u'opisane', self.ad.get_word(('przymiotnik', 'opis', {'liczba': 'mnoga', 'rodzaj': 'ĹĽ'})))

	def testGetWordNoun(self):
		self.assertEqual(u'znaku',  self.ad.get_word(('rzeczownik', 'znak', {'przypadek': 'dopeĹ‚niacz', 'liczba': 'pojedyncza'})))
		self.assertEqual(u'znakĂłw', self.ad.get_word(('rzeczownik', 'znak', {'przypadek': 'dopeĹ‚niacz', 'liczba': 'mnoga'})))

		self.assertEqual(u'znak',  self.ad.get_word(('rzeczownik', 'znak', {'przypadek': 'mianownik', 'liczba': 'pojedyncza'})))
		self.assertEqual(u'znaki', self.ad.get_word(('rzeczownik', 'znak', {'przypadek': 'mianownik', 'liczba': 'mnoga'})))

	def testGetConfPronoun(self):
		self.assertIn(('zaimek', 'ja', {'przypadek': 'miejscownik', 'liczba': 'pojedyncza', 'osoba': 'trzecia', 'rodzaj': 'ĹĽ'}), self.ad.get_conf('niej'))
		self.assertIn(('zaimek', 'ja', {'przypadek': 'miejscownik', 'liczba': 'pojedyncza', 'osoba': 'trzecia', 'rodzaj': 'm'}),  self.ad.get_conf('nim'))
		self.assertIn(('zaimek', 'ja', {'przypadek': 'miejscownik', 'liczba': 'mnoga', 'osoba': 'trzecia', 'rodzaj': 'm'}), self.ad.get_conf('nich'))

		self.assertEqual(('zaimek', 'ja', {'przypadek': 'mianownik', 'liczba': 'pojedyncza', 'osoba': 'trzecia', 'rodzaj': 'm'}),  self.ad.get_conf('on')[0])
		self.assertEqual(('zaimek', 'ja', {'przypadek': 'mianownik', 'liczba': 'pojedyncza', 'osoba': 'trzecia', 'rodzaj': 'ĹĽ'}), self.ad.get_conf('ona')[0])

		self.assertIn(('zaimek', 'ktĂłry', {'przypadek': 'miejscownik', 'liczba': 'pojedyncza', 'rodzaj': 'ĹĽ'}),  self.ad.get_conf('ktĂłrej'))
		self.assertIn(('zaimek', 'ktĂłry', {'przypadek': 'miejscownik', 'liczba': 'pojedyncza', 'rodzaj': 'mos'}),  self.ad.get_conf('ktĂłrym'))
		self.assertIn(('zaimek', 'ktĂłry', {'przypadek': 'miejscownik', 'liczba': 'mnoga', 'rodzaj': 'mos'}), self.ad.get_conf('ktĂłrych'))

	def testGetConfVerb(self):
		self.assertIn(('czasownik', 'nastÄ™powaÄ‡', {'aspekt': 'dokonane', 'forma': 'czas teraĹşniejszy', 'liczba': 'pojedyncza', 'osoba': 'pierwsza'}), self.ad.get_conf('nastÄ™puje'))
		self.assertEqual(('czasownik', 'nastÄ™powaÄ‡', {'aspekt': 'dokonane', 'forma': 'czas teraĹşniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'}), self.ad.get_conf('nastÄ™pujÄ…')[0])

		self.assertIn(('czasownik', 'wystÄ™powaÄ‡', {'aspekt': 'dokonane', 'forma': 'czas teraĹşniejszy', 'liczba': 'pojedyncza', 'osoba': 'pierwsza'}), self.ad.get_conf('wystÄ™puje'))
		self.assertEqual(('czasownik', 'wystÄ™powaÄ‡', {'aspekt': 'dokonane', 'forma': 'czas teraĹşniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'}), self.ad.get_conf('wystÄ™pujÄ…')[0])

		self.assertEqual(('czasownik', 'byÄ‡', {'aspekt': 'dokonane', 'forma': 'czas teraĹşniejszy', 'liczba': 'pojedyncza', 'osoba': 'trzecia'}), self.ad.get_conf('jest')[0])
		self.assertEqual(('czasownik', 'byÄ‡', {'aspekt': 'dokonane', 'forma': 'czas teraĹşniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'}),   self.ad.get_conf('sÄ…')[0])

	def testGetConfPreposition(self):
		self.assertEqual(('przyimek', 'z', {'forma': 'z'}),  self.ad.get_conf('z')[0])
		self.assertEqual(('przyimek', 'z', {'forma': 'ze'}), self.ad.get_conf('ze')[0])

	def testGetConfAdjective(self):
		self.assertEqual(('przymiotnik', 'opis', {'liczba': 'pojedyncza', 'rodzaj': 'm'}), self.ad.get_conf('opisany')[0])
		self.assertIn(('przymiotnik', 'opis', {'liczba': 'mnoga', 'rodzaj': 'm'}), self.ad.get_conf('opisane'))
		self.assertEqual(('przymiotnik', 'opis', {'liczba': 'pojedyncza', 'rodzaj': 'ĹĽ'}), self.ad.get_conf('opisana')[0])
		self.assertIn(('przymiotnik', 'opis', {'liczba': 'mnoga', 'rodzaj': 'ĹĽ'}), self.ad.get_conf('opisane'))

	def testGetConfNoun(self):
		self.assertIn(('rzeczownik', 'znak', {'przypadek': 'dopeĹ‚niacz', 'liczba': 'pojedyncza'}),  self.ad.get_conf('znaku'))
		self.assertEqual(('rzeczownik', 'znak', {'przypadek': 'dopeĹ‚niacz', 'liczba': 'mnoga'}), self.ad.get_conf('znakĂłw')[0])

		self.assertIn(('rzeczownik', 'znak', {'przypadek': 'mianownik', 'liczba': 'pojedyncza'}),  self.ad.get_conf('znak'))
		self.assertIn(('rzeczownik', 'znak', {'przypadek': 'mianownik', 'liczba': 'mnoga'}), self.ad.get_conf('znaki'))

if __name__ == '__main__':
	#import sys;sys.argv = ['', ''Test.test']
	unittest.main()
