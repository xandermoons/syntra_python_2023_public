'''
Print onderstaande patroon:
*
**
***
****
*****
****
***
**
*
'''

# Eerste manier
for i in range(1,6):
    print('*'*i)

for i in reversed(range(1,5)):
    print('*'*i)

print('')

# Tweede manier (omslachtig)
for i in range(1,2):
    print('*'*i)
    for j in range(2,3):
        print('*'*j)
        for k in range(3,4):
            print('*'*k)
            for l in range(4,5):
                print('*'*l)
                print('*'*(l+1))
                print('*'*l)
            print('*'*k)
        print('*'*j)
    print('*'*i)

print('')

# derde manier (gelijkaardig aan eerste manier)
lijst = [4,3,2,1]

for i in range(6):
    print('*'*i)

for i in lijst:
    print('*'*i)

print('')

# vierde manier (oplossing Olivier)
for i in range(1,7):
    if i < 6:
        print('*'*i)
    else:
        for j in range(6):
            print((6-j)*'*')

