getallen = []
sum = 0
for i in range(5):
    getal = input('Geef een getal in: ')
    getal = int(getal)
    getallen.append(getal)
    sum += getal

print(sum/5)