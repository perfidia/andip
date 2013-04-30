# -*- coding: utf-8 -*-

from andip import *

ad1 = PlWikiProvider()
# ad2 = FileProvider("../data/polish")#, backoff = ad1)
# ad3 = DatabaseProvider("../data/polish", backoff = ad2)

print ad1.get_word(('czasownik', 'być', {'aspekt': 'niedokonane', 'forma': 'czas terazniejszy', 'liczba': 'pojedyncza', 'osoba': 'trzecia'}))
print ad1.get_word(("czasownik", "występować", {'aspekt': 'niedokonane', 'forma': 'czas terazniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'}))
print ad1.get_word(("czasownik", "mieć", {'aspekt': 'niedokonane', 'forma': 'czas terazniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'}))
print ad1.get_word(("czasownik", "robić", {'aspekt': 'niedokonane', 'forma': 'czas terazniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'}))
print ad1.get_word(("czasownik", "robić", {'aspekt': 'niedokonane', 'forma': 'czas przeszly', 'liczba': 'pojedyncza', 'osoba': 'trzecia', 'rodzaj' : 'meski'}))
print ad1.get_word(("czasownik", "robić", {'aspekt': 'niedokonane', 'forma': 'czas terazniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'}))
print ad1.get_word(("czasownik", "robić", {'aspekt': 'niedokonane', 'forma': 'czas terazniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'}))
print ad1.get_word(("czasownik", "występować", {'aspekt': 'niedokonane', 'forma': 'czas przeszly', 'liczba': 'pojedyncza', 'osoba': 'trzecia', 'rodzaj' : 'meski'}))
print ad1.get_conf('robiłem')
print ad1.get_conf('robię')
print ad1.get_conf('robili')
print ad1.get_conf('występowałam')
print ad1.get_conf('występują')

print ad1.get_word(("czasownik", "występować", {'aspekt': 'niedokonane', 'forma': 'czas przeszly', 'liczba': 'pojedyncza', 'osoba': 'trzecia', 'rodzaj' : 'meski'}))
print ad1.get_word(('przymiotnik', 'żółty', {'przypadek' : 'dopełniacz', 'stopień' : 'wyższy', 'liczba': 'mnoga', 'rodzaj': 'm'}))
print ad1.get_word(('rzeczownik', 'pies', {'przypadek':'wołacz', 'liczba': 'mnoga'}));
print ad1.get_conf("żółtszym")                                            #
print ad1.get_conf('występują')                                           #
print ad1.get_conf('psie')
#
print ad1.get_word(("czasownik", "być", {'aspekt': 'niedokonane', 'forma': 'czas terazniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'}))
# ad3.save() # save new items to database

print ad1.get_word(('rzeczownik', 'pies', {'przypadek':'wołacz', 'liczba': 'pojedyncza'}));
print ad1.get_word(("czasownik", "występować", {'aspekt': 'niedokonane', 'forma': 'czas terazniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'}))
print ad1.get_word(('przymiotnik', 'żółty', {'przypadek' : 'celownik', 'stopień' : 'wyższy', 'liczba': 'mnoga', 'rodzaj': 'm'}))
print ad1.get_word(('przymiotnik', 'żółty', {'przypadek' : 'dopełniacz', 'stopień' : 'najwyższy', 'liczba': 'mnoga', 'rodzaj': 'm'}))
print ad1.get_word(('przymiotnik', 'żółty', {'przypadek' : 'celownik', 'stopień' : 'najwyższy', 'liczba': 'mnoga', 'rodzaj': 'm'}))
print ad1.get_word(('czasownik', 'być', {'aspekt' : 'niedokonane', 'forma': 'czas terazniejszy', 'liczba': 'pojedyncza', 'osoba': 'trzecia'}))
print ad1.get_word(('czasownik', 'być', {'aspekt': 'niedokonane', 'forma': 'czas terazniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'}))

######################TESTY DLA GET_CONF###################################
#ad = AnDiP(DatabaseProvider("../data/polish"))                           #
                                             #
##############################KONIEC#######################################

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
