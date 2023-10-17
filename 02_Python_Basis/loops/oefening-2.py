'''
Maak een lijst aan van studenten, hou van elke student het volgende bij: ID(unieke nummer), naam, voornaam,leeftijd, cursus
Vul dit op met 5 studenten, er zijn 2 cursussen "python" & "IT"
'''

# Olivier heeft een lijst gemaakt met mogelijke opleidingen en er naar verwezen in zijn cursus rubriek
# Hierdoor kan hij met een geneste loop 1. cursussen 2. studenten de namen printen zonder nieuwe lijsten te moeten maken

studenten = [{'ID' : "12345", "naam" : "De Roeck", "voornaam" : "Inias", "leeftijd": 30, "cursus" : "Python"},
             {'ID' : "23456", "naam" : "Moons", "voornaam" : "Xander", "leeftijd": 25, "cursus" : "IT"},
             {'ID' : "34567", "naam" : "Appeltans", "voornaam" : "Ruben", "leeftijd": 29, "cursus" : "IT"},
             {'ID' : "45678", "naam" : "Dewit", "voornaam" : "Peter", "leeftijd": 89, "cursus" : "IT"},
             {'ID' : "56789", "naam" : "Coppens", "voornaam" : "Jaak", "leeftijd": 45, "cursus" : "Python"}]


for student in studenten:
    print(f'{student["naam"]}, {student["voornaam"]}')

print()

leeftijden = set()
for student in studenten: 
    leeftijden.add(student['leeftijd'])

leeftijden = list(leeftijden)
for leeftijd in leeftijden:
    if(leeftijd == leeftijden[-1]):
        print(leeftijd)
    else:
        print(leeftijd, end = ', ')

print()

p = []
it = []

for student in studenten: 
    if(student["cursus"] == 'IT'):
        it.append([student["naam"], student["voornaam"]])
    elif(student["cursus"] == 'Python'):
        p.append([student["naam"], student["voornaam"]])

print(f"Python: {p}")
print(f'IT: {it}')


