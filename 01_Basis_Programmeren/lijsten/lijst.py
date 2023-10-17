lijst = []

for i in range(3):
    waarde = int(input('Geef een getal in: '))
    
    if waarde % 2 == 0:
        waarde /= 2
    lijst.append(waarde)

lijst.sort()
print(lijst)