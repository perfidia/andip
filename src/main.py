# -*- coding: utf-8 -*-

from andip import AnDiP
from andip.provider import FileProvider
from andip.provider.wiki import PlWikiProvider

#ad = AnDiP(FileProvider("../data/polish"))
ad = AnDiP(PlWikiProvider())

print 'opisany', ad.get_word(('przymiotnik', 'opis', {'liczba': 'pojedyncza', 'rodzaj': 'm'}))
print 'opisane', ad.get_word(('przymiotnik', 'opis', {'liczba': 'mnoga', 'rodzaj': 'm'}))
print 'opisana', ad.get_word(('przymiotnik', 'opis', {'liczba': 'pojedyncza', 'rodzaj': 'ż'}))
print 'opisane', ad.get_word(('przymiotnik', 'opis', {'liczba': 'mnoga', 'rodzaj': 'ż'}))

print ad.get_word(("czasownik", "występować", {'aspekt': 'dokonane', 'forma': 'czas teraźniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'}))
print ad.get_word(("czasownik", "występować", {'aspekt': 'dokonane', 'forma': 'czas przeszły', 'liczba': 'mnoga', 'osoba': 'trzecia'}))

print ad.get_conf("wystąpił")


print ad.get_word(('czasownik', 'być', {'forma': 'czas przesz\xc5\x82y', 'osoba': 'trzecia', 'aspekt': 'dokonane', 'liczba': 'pojedyncza'}))


#ad = AnDiP(FileProvider("../data/english"))
#
#print "am",  ad.get_word(('verb', 'be', {'number': 'singular', 'person': 'first'}))
#print "are", ad.get_word(('verb', 'be', {'number': 'singular', 'person': 'second'}))
#print "is",  ad.get_word(('verb', 'be', {'number': 'singular', 'person': 'third'}))
#
#print "are", ad.get_word(('verb', 'be', {'number': 'plural', 'person': 'first'}))
#print "are", ad.get_word(('verb', 'be', {'number': 'plural', 'person': 'second'}))
#print "are", ad.get_word(('verb', 'be', {'number': 'plural', 'person': 'third'}))
#
#print ad.get_conf("are")
