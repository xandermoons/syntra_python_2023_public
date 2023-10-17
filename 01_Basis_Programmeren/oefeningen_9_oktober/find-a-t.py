#Vraag de gebruiker om een tekst in te geven. Druk af als de letter 'a' en 't' in deze text voorkomen

text = input('Geef een tekst in: ')

def findLetters(text, letter1 = 'a', letter2 = 't'):
    return (letter1 in text) and (letter2 in text)

if findLetters(text):
    print(text)