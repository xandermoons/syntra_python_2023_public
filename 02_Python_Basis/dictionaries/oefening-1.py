'''
1. Maak een dictionary aan met 5 merken van wagens
2. Print deze lijst van merken en vraag de gebruiker welk merk van wagen hij heeft door het nummer in te geven
'''

my_cars = {
    1 : 'VW',
    2 : 'Citroen',
    3 : 'Fiat',
    4 : 'Seat',
    5 : 'Skoda'
}

for nummer, merk in my_cars.items():
    print(f'{nummer} --> {merk}')

keuze = int(input('Geef het nummer van het merk waar u mee rijdt: '))

print(f'U rijdt met een {my_cars[keuze]}')

# Oplossing Olivier:

'''
wagen = {}

wagen[1] = 'Audi'
wagen[2] = 'Toyota'
wagen[3] = 'BMW'
wagen[4] = 'Seat'
wagen[5] = 'Volkswagen'

for nummer, merk in wagen.items():
    print(f'Eagen type {nummer} is van het merk {merk}')

jouw_merk = int(input)('Welk type is uw wagen? ')
print(f'U rijdt met het merk {wagen[jouw_merk]}')

'''