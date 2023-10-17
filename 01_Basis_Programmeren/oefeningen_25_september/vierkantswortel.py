getal = input("Geef een getal: ")
getal = int(getal)

naukeurigheid = input('Tot hoeveel getallen na de komma? ')
naukeurigheid = int(naukeurigheid)

result = 0
schatter = 1
aantalloops = 0

for i in range(naukeurigheid+1):
    result += schatter
    while result**2 < getal:
        result += schatter
        aantalloops += 1
    if result**2 == getal: 
        break
    result -= schatter
    schatter *= 0.1

print(f'vierkantswortel = {round(result, naukeurigheid + 1)}')
print(f'{aantalloops} iteraties om aan de oplossing te komen')