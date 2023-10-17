# Functie om de faculteit te berekenen

n = input('Geef een getal in: ')

n = int(n)

result = 1

for i in range (1,n+1):
    result *= i

print(result)