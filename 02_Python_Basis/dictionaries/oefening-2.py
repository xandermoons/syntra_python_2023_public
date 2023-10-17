'''
Vraag een gebruiker om eigenschappen va neen wagen en bewaar dit in het geheugen.
De eigenschappen die we willen bewaren zijn merk, model, bouwjaar, kleur, prijs.
Nadat de gebruiker deze heeft ingegeven , duk alle wagen eigenschappen af

Doe nu hetzelfde voor meerdere wagens tot de gebruiker stopt
'''

# Functie om een nieuwe wagen toe te voegen
def nieuwe_wagen():
    merk = input('Merk: ')
    model = input('Model: ')
    bouwjaar = input('Bouwjaar: ')
    kleur = input('Kleur: ')
    prijs = input('Prijs: ')

    return {'merk' : merk, 
            'model' : model, 
            'bouwjaar' : bouwjaar, 
            'kleur' : kleur, 
            'prijs' : prijs
            }
    

wagens = {}
wagennummer = 1

while True:

    stop = input('Wilt u stoppen? Y/n: ' )

    # Stop de while-loop wanneer de input 'n' is
    if(stop == 'Y'):
        break
    
    # Hier wordt de nieuwe wagen toegevoegd aan de dictionary 'wagens' met behulp van bovenstaande functie
    wagens[wagennummer] = nieuwe_wagen()
    wagennummer += 1

print('\nHier zijn de wagens die u hebt toegevoegd: \n')

# De buitenste for-loop itereert over de wagens die toegevoegd zijn.
# De binnenste for-loop itereert over de key-value paren van de huidige wagen
for wagen in wagens.values():
    for key, value in wagen.items():
        print(f'{key} --> {value}')
    print()


# Oplossing Olivier:

# wagens = {}
# wagen_nummer = 0
# wagen_eigenschappen = ['merk', 'model']

# while True:
#     stop = input('Wilt u stoppen? Y/n: ' )

#     # Stop de while-loop wanneer de input 'n' is
#     if(stop != 'n'):
#         break

#     deze_wagen = {}
#     for eigenschap in wagen_eigenschappen:
#         deze_wagen[eigenschap] = input(f'Geef {eigenschap} van de wagen: ')
    
#     wagens[wagen_nummer] = deze_wagen

# print(wagens)