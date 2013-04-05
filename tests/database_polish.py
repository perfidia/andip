# -*- coding: utf-8 -*-

import unittest
from andip import AnDiP
from andip.provider import PlWikiProvider
from andip.provider import DatabaseProvider

class DatabasePolishTest(unittest.TestCase):

    def setUp(self):
        self.db = DatabaseProvider("../data/polish")
        self.ad1 = AnDiP(self.db)
        ad2 = AnDiP(PlWikiProvider("../data/polish"), self.ad1)
        ad2.get_word(('rzeczownik', 'pies', {'przypadek':'wołacz', 'liczba': 'mnoga'}))
#        ad2.get_word(("czasownik", "występować", {'aspekt': 'dokonane', 'forma': 'czas terazniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'}))
        ad2.get_word(('przymiotnik', 'żółty', {'przypadek' : 'dopełniacz', 'stopień' : 'wyższy', 'liczba': 'mnoga', 'rodzaj': 'm'}))
        ad2.save()

    def tearDown(self):
        self.db.close_database()

    def test_get_word(self):
        self.assertEquals(self.ad1.get_word(('rzeczownik', 'pies', {'przypadek':'mianownik', 'liczba': 'pojedyncza'})), 'pies')
        self.assertEquals(self.ad1.get_word(('przymiotnik', 'żółty', {'przypadek' : 'dopełniacz', 'stopień' : 'podstawowy', 'liczba': 'pojedyńcza', 'rodzaj': 'm'})), 'żółtego')
#        self.assertEquals(self.ad1.get_word(("czasownik", "występować", {'aspekt': 'dokonane', 'forma': 'czas terazniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'})), 'występują')
#        self.assertEquals(self.ad1.get_word(("czasownik", "występować", {'aspekt': 'niedokonane', 'forma': 'czas przeszly', 'liczba': 'mnoga', 'osoba': 'trzecia', 'rodzaj':'meski'})), "występowali")

if __name__ == '__main__':
	#import sys;sys.argv = ['', 'Test.test']
	unittest.main()
