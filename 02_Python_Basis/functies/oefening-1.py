'''
Maak een programma dat aan de gebruiker een ongekend aantal getallen vraagt en druk da de totale som af.
Maak gebruike van de global variabele
'''

def som():
    getallen = list()

    while True:
        getal = input("geef een getal in (schrijf 'STOP' wanneer u wil stoppen): ")
        
        if getal == 'STOP':
            break

        try:
            getal = float(getal)
        except ValueError as e:
            print('Foute input, geef een getal of "STOP" in')
            continue
        
        getallen.append(int(getal))
    
    return sum(getallen)

print(som())

