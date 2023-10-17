'''
Vraag de gebruiker om een ongekend aantal getallen, hou deze bij in een lijst en druk dan het volgende af
- de som van alle getallen
- welke getallen even zijnm welke getallen oneven zijnd
'''

getallen = list()
even = list()
oneven = list()

def som():

    while True:
        getal = input("geef een getal in (schrijf 'STOP' wanneer u wil stoppen): ")
        
        if getal == 'STOP':
            break

        try:
            getal = int(getal)
        except ValueError as e:
            print('Foute input, geef een getal of "STOP" in')
            continue
        
        getallen.append(int(getal))
        if getal % 2 == 0:
            even.append(getal)
        else: oneven.append(getal)


som()
print(f'Som van alle getallen: {sum(getallen)}')
print(f'Even getallen: {even}')
print(f'Oneven getallen: {oneven}')