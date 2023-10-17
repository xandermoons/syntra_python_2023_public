# Geef de laatste 2 nummers van een getal.

def laatste_twee(getal):
    return getal[-2:]

getal = input('Geef een getal van minstens twee cijfers: ')

while len(getal) < 2:
    getal = input('Getal is te kort. Geef een getal van minstens twee cijfers: ')

print(laatste_twee(getal))