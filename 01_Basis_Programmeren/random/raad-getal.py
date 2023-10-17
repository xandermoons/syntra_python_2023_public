# Maak een spel dat de gebruiker een getal tussen 1 en 20 moet raden. Als de gebruiker een cijfer ingeeft krijgt hij een hint of het kleiner of groter is.
# Voeg ook een optie toe zodtat de gebruiker kan stoppen indoen hij het spel beu is.

import random as rd

getal = rd.randint(1,20)

while True:
    w = input('Geef een getal tussen 1 en 20. Stop door "STOP" te typen: ')
    if('STOP' in w):
        print(f'U bent gestopt. Het getal was {getal}')
        break
    
    if w.isdigit():
        w = int(w)

        if(w==getal):
            print(f'Juist! het getal was {getal}')
            break
        elif(getal < w):
            print(f'Fout! het getal is lager dan {w}')
        else:
            print(f'Fout! Het getal is hoger dan {w}')
    else:
        print('De waarde die u hebt ingegeven is niet geldig, Probeer opnieuw')