# -*- coding: utf-8 -*-

import unittest
from andip import AnDiP
from andip.provider import PlWikiProvider
from andip.provider import DatabaseProvider

class DatabasePolishTest(unittest.TestCase):
    
    def setUp(self):
        self.wiki = PlWikiProvider("../data/Polish")
        self.ad = AnDiP(self.wiki)
        self.ad.get_word(("czasownik", "występować", {'aspekt': 'dokonane', 'forma': 'czas przeszły', 'liczba': 'mnoga', 'osoba': 'trzecia'}))
        self.wiki.close_database()
        self.database = DatabaseProvider("../data/Polish")
        self.ad = AnDiP(self.database)
        
    def tearDown(self):
        self.database.close_database()
        
    def test_get_word(self):
        self.assertEquals(self.ad.get_word(("czasownik", "występować", {'aspekt': 'niedokonane', 'forma': 'czas przeszly', 'liczba': 'mnoga', 'osoba': 'trzecia', 'rodzaj':'meski'})), "występowali") 
        