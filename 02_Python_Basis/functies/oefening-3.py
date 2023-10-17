'''
Maak een programma dat de gebruiker 5 namen en een salaris vraagt. Is er geen salaris dan nemen we als default 2000 euro. Druk deze lijst dan af
'''

mensen_lonen = list()

def toevoegen(naam, salaris=2000):
    persoon = {'naam': naam, 'salaris': salaris}
    mensen_lonen.append(persoon)

def gebruiker_input():
    for i in range(5):
        naam = input('Geef de naam van de persoon in: ')
        while True:

            salaris = input(f'Geef {naam} zijn salaris in: ')

            if salaris:
                try:
                    salaris = int(salaris)
                    toevoegen(naam, salaris)
                    break
                except ValueError as e:
                    print('Geen geldige input voor het salaris')
            else:
                toevoegen(naam)
                break     

def main():
    gebruiker_input()
    print(mensen_lonen)

main()