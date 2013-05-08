AnDiP
=====

Description
-----------

Dictionary for natural language generation. It contains data about declension, 
conjugation, ... (mainly for Polish an English language).

Installation
------------

### Simple

    python setup.py install

### Using eggs

    python setup.py bdist_egg
    cd dist
    easy_install <package_name>

Getting started
---------------

    from andip import *

    ad1 = PlWikiProvider()
    ad2 = DatabaseProvider("../data/polish", backoff = ad1)
    ad3 = FileProvider("../data/polish", backoff = ad2)

    print ad3.get_word(('czasownik', 'być', {'aspekt': 'niedokonane', 'forma': 'czas terazniejszy', 'liczba': 'pojedyncza', 'osoba': 'trzecia'}))
    print ad3.get_conf('jestem')

Authors
-------

See AUTHORS file.

License
-------

AnDiP is released under The MIT License. See LICENSE file.
