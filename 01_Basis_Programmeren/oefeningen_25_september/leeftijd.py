l = input('Geef uw leeftijd op: ')
l = int(l)

if l < 2: 
    print('Baby')
elif l < 4:
    print('Kleuter')
elif l < 11:
    print('Kind')
elif l < 18:
    print('Tiener')
else:
    print('Volwassene')