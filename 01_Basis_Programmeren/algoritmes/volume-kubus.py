# bereken het volume van een kubus

def volume_kubus(z):
    return z**3

z = input('Geef de lengte van de zijde van de kubus: ')

print(f'{volume_kubus(int(z))} kubieke meter')
