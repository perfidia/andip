# -*- coding: utf-8 -*-

from andip import AnDiP
from andip.provider import FileProvider, DatabaseProvider, PlWikiProvider

ad1 = AnDiP(FileProvider("../data/polish"))
ad2 = AnDiP(DatabaseProvider("../data/polish"), backoff=ad1)
ad3 = AnDiP(PlWikiProvider(), backoff=ad2)

print ad3.get_word(("czasownik", "występować", {'aspekt': 'dokonane', 'forma': 'czas teraźniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'}))
print ad3.get_word(('przymiotnik', 'żółty', {'przypadek' : 'dopełniacz', 'stopień' : 'wyższy', 'liczba': 'mnoga', 'rodzaj': 'm'}))
print ad3.get_word(('rzeczownik', 'pies', {'przypadek':'wołacz', 'liczba': 'mnoga'}));

ad3.save() # save new items to database

print ad2.get_word(('rzeczownik', 'pies', {'przypadek':'wołacz', 'liczba': 'pojedyncza'}));
print ad2.get_word(("czasownik", "występować", {'aspekt': 'dokonane', 'forma': 'czas teraźniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'}))
print ad2.get_word(('przymiotnik', 'żółty', {'przypadek' : 'celownik', 'stopień' : 'wyższy', 'liczba': 'mnoga', 'rodzaj': 'm'}))
print ad2.get_word(('przymiotnik', 'żółty', {'przypadek' : 'dopełniacz', 'stopień' : 'najwyższy', 'liczba': 'mnoga', 'rodzaj': 'm'}))
print ad2.get_word(('przymiotnik', 'żółty', {'przypadek' : 'celownik', 'stopień' : 'najwyższy', 'liczba': 'mnoga', 'rodzaj': 'm'}))

######################TESTY DLA GET_CONF###################################
#ad = AnDiP(DatabaseProvider("../data/polish"))                           #
#print ad.get_conf("żółtszym")                                            #
#print ad.get_conf('występują')                                           #
#print ad.get_conf('psie')                                                #
##############################KONIEC#######################################

#print ad.get_conf('najżółtszych')
#print ad.get_conf('najżółtszym')
#print ad.get_conf('żółtszych')
#print ad.get_conf('żółtszym')
#print 'opisany', ad.get_word(('przymiotnik', 'opis', {'liczba': 'pojedyncza', 'rodzaj': 'm'}))
#print 'opisane', ad.get_word(('przymiotnik', 'opis', {'liczba': 'mnoga', 'rodzaj': 'm'}))
#print 'opisana', ad.get_word(('przymiotnik', 'opis', {'liczba': 'pojedyncza', 'rodzaj': 'ż'}))
#print 'opisane', ad.get_word(('przymiotnik', 'opis', {'liczba': 'mnoga', 'rodzaj': 'ż'}))
#
#print ad.get_word(("czasownik", "występować", {'aspekt': 'dokonane', 'forma': 'czas przeszły', 'liczba': 'mnoga', 'osoba': 'trzecia'}))
#
#print ad.get_word("występować")

#db = DatabaseProvider.DatabaseProvider('Data')
#print db.get_verb({'aspekt' : 'niedokonane', 'forma' : 'czas terazniejszy', 'liczba' : 'mnoga', 'osoba': 'trzecia'}, 'występować')
#print db.get_verb({'aspekt' : 'niedokonane', 'forma' : 'czas terazniejszy', 'liczba' : 'mnoga', 'osoba': 'trzecia'}, 'zabierać')

#print ad.get_conf('występować')

#print ad.get_word(('przymiotnik', 'zachodni', {'stopień': 'podstawowy', 'przypadek' : 'dopełniacz', 'liczba': 'mnoga', 'rodzaj': 'm'}))
#print ad.get_word(('czasownik', 'występować', {'aspekt' : 'niedokonane', 'forma' : 'czas terazniejszy', 'liczba' : 'mnoga', 'osoba': 'trzecia'}))
#print ad.get_word(('czasownik', 'występować', {'aspekt' : 'niedokonane', 'forma' : 'czas terazniejszy', 'liczba' : 'pojedyncza', 'osoba': 'trzecia'}))
#print ad.get_word(('czasownik', 'występować', {'aspekt' : 'niedokonane', 'forma' : 'czas terazniejszy', 'liczba' : 'mnoga', 'osoba': 'pierwsza'}))
#print ad.get_word(('czasownik', 'występować', {'aspekt' : 'niedokonane', 'forma' : 'czas terazniejszy', 'liczba' : 'mnoga', 'osoba': 'druga'}))
#print ad.get_word(('czasownik', 'występować', {'aspekt' : 'niedokonane', 'forma' : 'czas terazniejszy', 'liczba' : 'pojedyncza', 'osoba': 'druga'}))

#print ad.get_word(('czasownik', 'występować', {'aspekt' : 'niedokonane', 'forma' : 'czas terazniejszy', 'liczba' : 'mnoga', 'osoba': 'trzecia'}))
#print ad.get_conf("występować")
#print ad.get_conf("piękny")
#print ad.get_conf("zdrowy")
#print ad.get_conf("zachodni")
#print ad.get_conf("zdrów")
#print ad.get_conf('kot')

#
#print ad.get_word(('czasownik', 'być', {'forma': 'czas przesz\xc5\x82y', 'osoba': 'trzecia', 'aspekt': 'dokonane', 'liczba': 'pojedyncza'}))
