# Bereken de oppervlakte van een driehoek

def oppervlakte_driehoek(basis,hoogte):
    return basis*hoogte/2

b = input('Geef de basis van de driehoek: ')
h = input('Geef de hoogte van de drieboek: ')

print(f'{oppervlakte_driehoek(int(b), int(h))} vierkante meter')