# -*- coding: utf-8 -*-

import os
import tempfile
import unittest

from andip import AnDiP
from andip.provider import PlWikiProvider
from andip.provider import DatabaseProvider

class DatabasePolishTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fd_tmp = tempfile.NamedTemporaryFile()

        cls.ad_db = AnDiP(DatabaseProvider(cls.fd_tmp.name))
        ad_wi = AnDiP(PlWikiProvider(), backoff=cls.ad_db)

        print cls.fd_tmp.name

        ad_wi.get_word(('rzeczownik', 'pies', {'przypadek':'wołacz', 'liczba': 'mnoga'}))
        ad_wi.get_word(('przymiotnik', 'żółty', {'przypadek' : 'dopełniacz', 'stopień' : 'wyższy', 'liczba': 'mnoga', 'rodzaj': 'm'}))
        #ad_wi.get_word(("czasownik", "występować", {'aspekt': 'dokonane', 'forma': 'czas terazniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'}))

        ad_wi.save()

    @classmethod
    def tearDownClass(cls):
        cls.ad_db.close()
        os.remove(cls.fd_tmp.name + ".fs")
        os.remove(cls.fd_tmp.name + ".fs.index")
        os.remove(cls.fd_tmp.name + ".fs.lock")
        os.remove(cls.fd_tmp.name + ".fs.tmp")
        cls.fd_tmp.close()

    def testGetWord(self):
        self.assertEquals(self.ad_db.get_word(('rzeczownik', 'pies', {'przypadek':'mianownik', 'liczba': 'pojedyncza'})), 'pies')
        self.assertEquals(self.ad_db.get_word(('przymiotnik', 'żółty', {'przypadek' : 'dopełniacz', 'stopień' : 'podstawowy', 'liczba': 'pojedyńcza', 'rodzaj': 'm'})), 'żółtego')


#        print self.ad_db.get_conf('pies')
#        self.assertEquals(self.ad1.get_word(("czasownik", "występować", {'aspekt': 'dokonane', 'forma': 'czas terazniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'})), 'występują')
#        self.assertEquals(self.ad1.get_word(("czasownik", "występować", {'aspekt': 'niedokonane', 'forma': 'czas przeszly', 'liczba': 'mnoga', 'osoba': 'trzecia', 'rodzaj':'meski'})), "występowali")

if __name__ == '__main__':
    #import sys;sys.argv = ['', 'Test.test']
    unittest.main()
