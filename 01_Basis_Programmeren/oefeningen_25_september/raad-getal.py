import random as rd

getal = rd.randint(1,10)

n = input('raad het getal tussen 1 en 10')
n = int(n)
while n != getal:
    print('getal is niet juist. Probeer opnieuw')
    n = input('geef een ander getal in')
    n = int(n)
print('Getal is juist!')