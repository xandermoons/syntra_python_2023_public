# Schrijf 4 functies goLeft(), goRight()m goUp(), goDown() die de richting printen die je uitgaat. Schrijf een programma
# dat de gebruiker 1 richting vraagt, en gebruik de functies om deze richting te printen.

def goLeft():
    print('You went left')

def goRight():
    print('You wen right')

def goUp():
    print('You went up')

def goDown():
    print('You went down')



i = input('Choose the direction you want to go: ')
i = i.lower()

if i == 'left':
    goLeft()
elif i == 'right':
    goRight()
elif i == 'up':
    goUp()
elif i == 'down':
    goDown()
else:
    print('Wrong input. Please try again')