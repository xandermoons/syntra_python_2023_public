# Vraag de gebruiker om een gatal tussen 1 en 60 in te geven. Druk alle cijfers af die je kan delen door 9

getal = int(input('Geef een getal in tussen 1 en 60: '))

for i in range(getal):
    if i % 9 == 0:
        print(i)
