'''
Maak een lijst met volgende steden: Kortrijk, Gent, Antwerpen, Mechelen, Kluisbergen, Brussel, Brugge, 
Sint-Niklaas, Bornem, Luik, CHarleroi
Kies er random 3 uit via een random selectie op de index. Indien de index even is, vervang je de naam door streepjes
indien de index oneven is door sterretjes. Print de lijst af waarbij de vervangingen zijn doorgevoerd
'''

import random as rd
import numpy as np

steden = ['Kortrijk', 'Gent', 'Antwerpen', 'Mechelen', 'Kluisbergen', 'Brussel', 'Brugge', 
          'Sint-Niklaas', 'Bornem', 'Luik', 'Charleroi']

indices = list(np.arange(len(steden)))
js = rd.sample(indices,3)

for i in js:

    stad = steden[i]

    if i % 2 == 0:
        stad = '-'*len(stad)
    
    else: 
        stad = '*'*len(stad)
    
    steden[i] = stad

print(steden)
