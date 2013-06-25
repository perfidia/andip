# -*- coding: utf-8 -*-

from andip import *

ad1 = PlWikiProvider()
ad2 = DatabaseProvider("../data/polish", backoff = ad1)
ad3 = FileProvider("../data/polish", backoff = ad2)


print ad1.get_word(("czasownik", "występować", {'aspekt': 'niedokonane', 'forma': 'czas przyszły', 'liczba': 'mnoga', 'osoba': 'trzecia', 'rodzaj': 'm'}))




print ad1.get_word(('czasownik', 'narysować', {'aspekt': 'dokonane', 'forma': 'czas przyszły', 'liczba': 'pojedyncza', 'osoba': 'pierwsza'}))
print ad1.get_conf('narysuję')		
print ad1.get_conf('narysujesz') 	
print ad1.get_conf('narysuje')		
print ad1.get_conf('narysujemy') 	
print ad1.get_conf('narysujecie') 	
print ad1.get_conf('narysują')
print ad1.get_conf('będą występowali')
print ad3.get_word(('czasownik', 'być', {'aspekt': 'niedokonane', 'forma': 'czas teraźniejszy', 'liczba': 'pojedyncza', 'osoba': 'trzecia'}))
print ad3.get_word(("czasownik", "występować", {'aspekt': 'niedokonane', 'forma': 'czas teraźniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'}))
print ad3.get_word(("czasownik", "robić", {'aspekt': 'niedokonane', 'forma': 'czas teraźniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'}))
print ad3.get_word(("czasownik", "robić", {'aspekt': 'niedokonane', 'forma': 'czas przeszły', 'liczba': 'pojedyncza', 'osoba': 'trzecia', 'rodzaj' : 'm'}))
print ad3.get_word(("czasownik", "robić", {'aspekt': 'niedokonane', 'forma': 'czas teraźniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'}))
print ad3.get_word(("czasownik", "robić", {'aspekt': 'niedokonane', 'forma': 'czas teraźniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'}))
# ad3.save_model(ad1.get_model())
print ad3.get_word(("czasownik", "występować", {'aspekt': 'niedokonane', 'forma': 'czas przeszły', 'liczba': 'pojedyncza', 'osoba': 'trzecia', 'rodzaj' : 'm'}))
print ad3.get_word(('przymiotnik', 'żółty', {'przypadek' : 'dopełniacz', 'stopień' : 'wyższy', 'liczba': 'mnoga', 'rodzaj': 'm'}))
print ad3.get_word(('rzeczownik', 'pies', {'przypadek':'wołacz', 'liczba': 'mnoga'}));
print ad3.get_conf("żółtszych")                                            #
print ad3.get_conf('występują')                                           #
print ad3.get_conf('psie')
print ad3.get_word(("czasownik", "być", {'aspekt': 'niedokonane', 'forma': 'czas teraźniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'}))
print ad3.get_word(('rzeczownik', 'pies', {'przypadek':'wołacz', 'liczba': 'pojedyncza'}));
print ad3.get_word(("czasownik", "występować", {'aspekt': 'niedokonane', 'forma': 'czas teraźniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'}))
print ad3.get_word(('przymiotnik', 'żółty', {'przypadek' : 'celownik', 'stopień' : 'wyższy', 'liczba': 'mnoga', 'rodzaj': 'm'}))
print ad3.get_word(('przymiotnik', 'żółty', {'przypadek' : 'dopełniacz', 'stopień' : 'najwyższy', 'liczba': 'mnoga', 'rodzaj': 'm'}))
print ad3.get_word(('przymiotnik', 'żółty', {'przypadek' : 'celownik', 'stopień' : 'najwyższy', 'liczba': 'mnoga', 'rodzaj': 'm'}))
print ad3.get_word(('czasownik', 'być', {'aspekt' : 'niedokonane', 'forma': 'czas teraźniejszy', 'liczba': 'pojedyncza', 'osoba': 'trzecia'}))
print ad3.get_word(('czasownik', 'być', {'aspekt': 'niedokonane', 'forma': 'czas teraźniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'}))

print ad1.get_word(("czasownik", "występować", {'aspekt': 'niedokonane', 'forma': 'czas teraźniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'}))
print ad1.get_word(("czasownik", "robić", {'aspekt': 'niedokonane', 'forma': 'czas teraźniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'}))

ad1.get_conf('robiłem')
ad1.get_conf('robię')
ad1.get_conf('robili')
ad1.get_conf('występowałam')
ad1.get_conf('występują')

print "model", ad1.get_model()
ad2.save_model(ad1.get_model())
print ad2.get_word(('czasownik', 'być', {'aspekt': 'niedokonane', 'forma': 'czas teraźniejszy', 'liczba': 'pojedyncza', 'osoba': 'trzecia'}))
print ad2.get_word(("czasownik", "występować", {'aspekt': 'niedokonane', 'forma': 'czas teraźniejszy', 'liczba': 'mnoga', 'osoba': 'trzecia'}))

print ad2.get_conf('robiłem')
print ad2.get_conf('robię')
print ad2.get_conf('robili')
print ad2.get_conf('występowałam')
print ad2.get_conf('występują')

ad2.close()

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
#print db.get_verb({'aspekt' : 'niedokonane', 'forma' : 'czas teraźniejszy', 'liczba' : 'mnoga', 'osoba': 'trzecia'}, 'występować')
#print db.get_verb({'aspekt' : 'niedokonane', 'forma' : 'czas teraźniejszy', 'liczba' : 'mnoga', 'osoba': 'trzecia'}, 'zabierać')

#print ad.get_conf('występować')

#print ad.get_word(('przymiotnik', 'zachodni', {'stopień': 'podstawowy', 'przypadek' : 'dopełniacz', 'liczba': 'mnoga', 'rodzaj': 'm'}))
#print ad.get_word(('czasownik', 'występować', {'aspekt' : 'niedokonane', 'forma' : 'czas teraźniejszy', 'liczba' : 'mnoga', 'osoba': 'trzecia'}))
#print ad.get_word(('czasownik', 'występować', {'aspekt' : 'niedokonane', 'forma' : 'czas teraźniejszy', 'liczba' : 'pojedyncza', 'osoba': 'trzecia'}))
#print ad.get_word(('czasownik', 'występować', {'aspekt' : 'niedokonane', 'forma' : 'czas teraźniejszy', 'liczba' : 'mnoga', 'osoba': 'pierwsza'}))
#print ad.get_word(('czasownik', 'występować', {'aspekt' : 'niedokonane', 'forma' : 'czas teraźniejszy', 'liczba' : 'mnoga', 'osoba': 'druga'}))
#print ad.get_word(('czasownik', 'występować', {'aspekt' : 'niedokonane', 'forma' : 'czas teraźniejszy', 'liczba' : 'pojedyncza', 'osoba': 'druga'}))

#print ad.get_word(('czasownik', 'występować', {'aspekt' : 'niedokonane', 'forma' : 'czas teraźniejszy', 'liczba' : 'mnoga', 'osoba': 'trzecia'}))
#print ad.get_conf("występować")
#print ad.get_conf("piękny")
#print ad.get_conf("zdrowy")
#print ad.get_conf("zachodni")
#print ad.get_conf("zdrów")
#print ad.get_conf('kot')

#
#print ad.get_word(('czasownik', 'być', {'forma': 'czas przesz\xc5\x82y', 'osoba': 'trzecia', 'aspekt': 'dokonane', 'liczba': 'pojedyncza'}))
