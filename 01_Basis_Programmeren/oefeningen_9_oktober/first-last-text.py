# Vraag de gebruiker om een tekst in te geven. Druk hiervan de eerste 3 letters en de laatste 3 letters af

text = input('Geef een tekst in van minstens 3 karakters die geen spaties zijn: ')
text = text.strip()

if(len(text) < 3):
    print('De tekst is niet lang genoeg')
    exit()

def firstThree(text):
    return text[:3]

def lastThree(text):
    return text[-3:]

print(f'Eerste 3 letters: {firstThree(text)}\nLaatste 3 letters: {lastThree(text)}')