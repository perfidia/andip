# -*- coding: utf-8 -*-

from andip import AnDiP
from andip.provider import FileProvider
from andip.provider.wiki import PlWikiProvider
from andip.provider import database

ad = AnDiP(FileProvider("../data/polish"))
ad = AnDiP(PlWikiProvider())

#print 'opisany', ad.get_word(('przymiotnik', 'opis', {'liczba': 'pojedyncza', 'rodzaj': 'm'}))
#print 'opisane', ad.get_word(('przymiotnik', 'opis', {'liczba': 'mnoga', 'rodzaj': 'm'}))
#print 'opisana', ad.get_word(('przymiotnik', 'opis', {'liczba': 'pojedyncza', 'rodzaj': 'ż'}))
#print 'opisane', ad.get_word(('przymiotnik', 'opis', {'liczba': 'mnoga', 'rodzaj': 'ż'}))
#
#print ad.get_word(("czasownik", "występować", {'aspekt': 'dokonane', 'forma': 'czas teraźniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'}))
#print ad.get_word(("czasownik", "występować", {'aspekt': 'dokonane', 'forma': 'czas przeszły', 'liczba': 'mnoga', 'osoba': 'trzecia'}))
#
#print ad.get_word("występować")
#print ad.get_word("srać")

#db = DatabaseProvider.DatabaseProvider('Data')
#print db.get_verb({'aspekt' : 'niedokonane', 'forma' : 'czas terazniejszy', 'liczba' : 'mnoga', 'osoba': 'trzecia'}, 'występować')
#print db.get_verb({'aspekt' : 'niedokonane', 'forma' : 'czas terazniejszy', 'liczba' : 'mnoga', 'osoba': 'trzecia'}, 'zabierać')

#print ad.get_conf('występować')
print ad.get_word(('czasownik', 'występować', {'aspekt' : 'niedokonane', 'forma' : 'czas terazniejszy', 'liczba' : 'mnoga', 'osoba': 'trzecia'}))
#print ad.get_conf("występować")
#print ad.get_conf("srać")
#print ad.get_conf("piękny")
#print ad.get_conf("zdrowy")
#print ad.get_conf("zachodni")
#print ad.get_conf("zdrów")
print ad.get_word(('rzeczownik', 'kot', {'przypadek':'Wołacz', 'liczba': 'mnoga'}));
print ad.get_conf('kot')

#
#print ad.get_word(('czasownik', 'być', {'forma': 'czas przesz\xc5\x82y', 'osoba': 'trzecia', 'aspekt': 'dokonane', 'liczba': 'pojedyncza'}))
