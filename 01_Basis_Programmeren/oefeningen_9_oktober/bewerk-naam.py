# Vraag de gebruiker om zijn voornaam en familienaam> Druk deze af in hoofdletters, kleine letters en camelcase

first_name = input('Geef uw voornaam in: ')
name = input('Geef uw naam in: ')

def camelCase(word):
    word_list  = [word[:1],  word[1:]]
    word = word_list[0].upper() + word_list[1].lower()
    return word

def upperCase(word):
    return word.upper()

def lowerCase(word):
    return word.lower()

print(f'Camelcase: {camelCase(first_name)} {camelCase(name)}')
print(f'Uppercase: {upperCase(first_name)} {upperCase(name)}')
print(f'Lowercase: {lowerCase(first_name)} {lowerCase(name)}')