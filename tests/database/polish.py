# -*- coding: utf-8 -*-

import os
import unittest

from andip import AnDiP
from andip.provider import PlWikiProvider
from andip.provider import DatabaseProvider

class DatabasePolishTest(unittest.TestCase):
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

        cls.db = DatabaseProvider(os.sep.join(path))
        cls.ad_data = AnDiP(cls.db)
        ad_wiki = AnDiP(PlWikiProvider(os.sep.join(path)), backoff=cls.ad_data)

        ad_wiki.get_word(('rzeczownik', 'pies', {'przypadek':'wołacz', 'liczba': 'mnoga'}))
        ad_wiki.get_word(('przymiotnik', 'żółty', {'przypadek' : 'dopełniacz', 'stopień' : 'wyższy', 'liczba': 'mnoga', 'rodzaj': 'm'}))

        ad_wiki.save()

    @classmethod
    def tearDownClass(cls):
        cls.db.close()

    def test_get_word(self):
        self.assertEquals(self.db.get_word(('rzeczownik', 'pies', {'przypadek':'mianownik', 'liczba': 'pojedyncza'})), 'pies')
        self.assertEquals(self.db.get_word(('przymiotnik', 'żółty', {'przypadek' : 'dopełniacz', 'stopień' : 'podstawowy', 'liczba': 'pojedyńcza', 'rodzaj': 'm'})), 'żółtego')
#        self.assertEquals(self.ad1.get_word(("czasownik", "występować", {'aspekt': 'dokonane', 'forma': 'czas terazniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'})), 'występują')
#        self.assertEquals(self.ad1.get_word(("czasownik", "występować", {'aspekt': 'niedokonane', 'forma': 'czas przeszly', 'liczba': 'mnoga', 'osoba': 'trzecia', 'rodzaj':'meski'})), "występowali")

if __name__ == '__main__':
    #import sys;sys.argv = ['', 'Test.test']
    unittest.main()
