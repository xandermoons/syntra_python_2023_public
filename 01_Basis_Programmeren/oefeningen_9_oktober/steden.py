'''
Maak een lijst met volgende steden: Kortrijk, Gent, Antwerpen, Mechelen, Kluisbergen, Brussel, Brugge, 
Sint-Niklaas, Bornem, Luik, CHarleroi
Kies er random 3 uit via een random selectie op de index. Indien de index even is, vervang je de naam door streepjes
indien de index oneven is door sterretjes. Print de lijst af waarbij de vervangingen zijn doorgevoerd
'''
import random as rd

steden = ['Kortrijk', 'Gent', 'Antwerpen', 'Mechelen', 'Kluisbergen', 'Brussel', 'Brugge', 
          'Sint-Niklaas', 'Bornem', 'Luik', 'Charleroi']

indices = []

for i in range(3):
    j = -1
    while j in indices:
        j = rd.randint(0,len(steden) - 1)

    indices.append(j)

    stad = steden[j]

    if j % 2 == 0:
        stad = '-'*len(stad)
    
    else: 
        stad = '*'*len(stad)
    
    steden[j] = stad

print(steden)
