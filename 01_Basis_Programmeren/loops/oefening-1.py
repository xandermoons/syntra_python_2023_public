# Vraag de gebruiker om een getal tussen 1 en 10 in te geven. Druk dan alle voorgaande nummers af.

getal = int(input('Geef een getal in tussen 1 en 10: '))

for i in range(getal):
    print(i)