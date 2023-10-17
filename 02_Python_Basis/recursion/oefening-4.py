'''
Vraag de gebruiker om een getalm als hij 5 x verkeerd is stop dan het programma, 
anders druk het af, maak uiteraard gebruik van een recursieve functie
'''

import random as rd

getal = rd.randint(1,20)
print(getal)

def gok_getal(pogingen):
    if pogingen <= 0:
        return False
    
    gok = gok_input()

    if(gok == getal):
        return True
    
    if(pogingen == 1) :
        print('Fout!')
    else: 
        print(f'Fout! u heeft nog {pogingen - 1} pogingen')

    return gok_getal(pogingen-1)

def gok_input():
    gok = input('Gok het getal tussen 0 en 20: ')
    try:
        gok = int(gok)
        if gok <= 0 or gok > 20:
            print('Dit is geen geldig getal')
            gok_input()
        return gok
    except:
        print('Dit is geen geldig getal')
        gok_input()
    

def main():
    b = gok_getal(5)
    if b:
        print('Juist! Goed bezig')
    else:
        print(f'U heeft het getal niet kunnen raden. Het getal was {getal}')

main()