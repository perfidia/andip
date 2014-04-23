# -*- coding: utf-8 -*-
from andip.neo4j import Neo4JProvider
from andip.arangodb import ArangoProvider
from andip import PlWikiProvider
import json

data = eval(open("../data/polish.txt").read())
def neo4jExample(dataToImport):
    conf = "http://localhost:7474/db/data/"
    provider =  Neo4JProvider(conf)
    provider.dropAll()
    provider.importData(dataToImport)
    print provider.get_conf('ja')
    print provider.get_word(('czasownik', 'być', {'forma': 'czas teraźniejszy', 'liczba': 'pojedyncza', 'osoba': 'trzecia'}))
    wiki = PlWikiProvider()
    provider =  Neo4JProvider(conf,wiki)
    print provider.get_word(('czasownik', 'narysować', {'aspekt': 'dokonane', 'forma': 'czas przyszły', 'liczba': 'pojedyncza', 'osoba': 'pierwsza'}))
    print provider.get_conf('narysuję')

def arangoExample(dataToImport):
    provider =  ArangoProvider()
    provider.dropAll()
    provider.importData(dataToImport)
    print provider.get_conf('ja')
    print provider.get_word(('czasownik', 'być', {'forma': 'czas teraźniejszy', 'liczba': 'pojedyncza', 'osoba': 'trzecia'}))
    wiki = PlWikiProvider()
    provider =  ArangoProvider(wiki)
    print provider.get_word(('czasownik', 'narysować', {'aspekt': 'dokonane', 'forma': 'czas przyszły', 'liczba': 'pojedyncza', 'osoba': 'pierwsza'}))
    print provider.get_conf('narysuję')

if __name__ == '__main__':
    neo4jExample(data)
    arangoExample(data)