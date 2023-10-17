'''
Maak een lottoformulier met een nested loop en print dit af. Een lotto formulier zier er zo uit:
1 2 3 4 5
6 7 8 9 10
...
41 42 43 44 45
Maak dit ook zonder een nested loop te gebruiken
'''
# Met nested loop:

for i in range(1,46,5):

    for j in range(5):
        print(j+i, end='\t')
    
    print()

print()

# Zonder nested loop:

for i in range(1,46):

    if(i%5 == 0):
        print(i)
    else: 
        print(i, end='\t')

print()

# oplossing Olivier:

lottonummer = 1

for rij in range(9):
    for kolom in range(5):
        print(lottonummer, end = '\t')
        lottonummer += 1
    print()