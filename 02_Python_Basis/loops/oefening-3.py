'''
Maak een lotto spel. Vraag de gebruikem om 6 getallen en druk dan af als hij een winnende combinatie heeft

'''

# nummers invoeren makkelijker via recursie oproept bij fout

import random as rd
import numpy as np

print('--- Lotto ---')
print('--- Kies uw 6 cijfers ---')

keuze_getallen = list(np.arange(1,46))

getallen_gebruiker = set()
getallen_computer = set(rd.sample(range(1,46), 6))

for i in range(1,7):
    while True:
        getal = input(f'Geef een getal op (getal {i}): ')

        if getal.isdigit():
            getal = int(getal)

            if(getal in keuze_getallen) and (getal not in getallen_gebruiker):
                getallen_gebruiker.add(getal)
                break
        print('Dit getal hebt u al kozen of bestaat niet. Probeer opnieuw')

getallen_gewonnen = getallen_gebruiker.intersection(getallen_computer)

print(f'\nDe winnende combinatie is: {list(getallen_computer)}')
print('We gaan nu kijken of u gewonnen heeft\n')

if(len(getallen_gewonnen) != 0):
    print(f'Aantal correcte cijfers: {len(getallen_gewonnen)}')
    print(f'De volgende cijfers zijn correct: {list(getallen_gewonnen)}')
else:
    print('Haha loser niks gewonnen')