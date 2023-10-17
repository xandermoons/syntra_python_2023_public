import random as rd
import numpy as np

keuze_getallen =  list(np.arange(1,46))

def gebruiker_input():
    getallen_gebruiker = set()
    for i in range(1,7):
        while True:
            getal = input(f'Geef een getal op (getal {i}): ')

            if getal.isdigit():
                getal = int(getal)

                if(getal in keuze_getallen) and (getal not in getallen_gebruiker):
                    getallen_gebruiker.add(getal)
                    break
            print('Dit getal hebt u al kozen of bestaat niet. Probeer opnieuw')
    return getallen_gebruiker

def computer_input():
    return set(rd.sample(range(1,46), 6))

def gewonnen(gewonnen_getallen):
    if(len(gewonnen_getallen) != 0):
        print(f'Aantal correcte cijfers: {len(gewonnen_getallen)}')
        print(f'De volgende cijfers zijn correct: {list(gewonnen_getallen)}')
    else:
        print('Haha loser niks gewonnen')


def main():
    print('--- Lotto ---')
    print('--- Kies uw 6 cijfers ---')

    getallen_gebruiker = gebruiker_input()
    getallen_computer = computer_input()

    print(f'\nDe winnende combinatie is: {list(getallen_computer)}')
    print('We gaan nu kijken of u gewonnen heeft\n')

    gewonnen(getallen_gebruiker.intersection(getallen_computer))

main()
    





