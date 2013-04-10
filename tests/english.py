# -*- coding: utf-8 -*-

import unittest
from andip import AnDiP
from andip.provider import FileProvider

class PolishTest(unittest.TestCase):
	def setUp(self):
		self.ad = AnDiP(FileProvider('../data/english'))

	def testGetWordVerb(self):
		self.assertEqual(u'am',  self.ad.get_word(('verb', 'be', {'number': 'singular', 'person': 'first'})))
		self.assertEqual(u'are', self.ad.get_word(('verb', 'be', {'number': 'singular', 'person': 'second'})))
		self.assertEqual(u'is',  self.ad.get_word(('verb', 'be', {'number': 'singular', 'person': 'third'})))

		self.assertEqual(u'are', self.ad.get_word(('verb', 'be', {'number': 'plural', 'person': 'first'})))
		self.assertEqual(u'are', self.ad.get_word(('verb', 'be', {'number': 'plural', 'person': 'second'})))
		self.assertEqual(u'are', self.ad.get_word(('verb', 'be', {'number': 'plural', 'person': 'third'})))

	def testGetConfVerb(self):
		self.assertEqual(('verb', 'be', {'number': 'singular', 'person': 'first'}),  self.ad.get_conf('am')[0])
		self.assertIn   (('verb', 'be', {'number': 'singular', 'person': 'second'}),  self.ad.get_conf('are'))
		self.assertEqual(('verb', 'be', {'number': 'singular', 'person': 'third'}),  self.ad.get_conf('is')[0])
		self.assertIn   (('verb', 'be', {'number': 'plural', 'person': 'first'}),  self.ad.get_conf('are'))
		self.assertIn   (('verb', 'be', {'number': 'plural', 'person': 'second'}),  self.ad.get_conf('are'))
		self.assertIn   (('verb', 'be', {'number': 'plural', 'person': 'third'}),  self.ad.get_conf('are'))

if __name__ == '__main__':
	#import sys;sys.argv = ['', 'Test.test']
	unittest.main()
