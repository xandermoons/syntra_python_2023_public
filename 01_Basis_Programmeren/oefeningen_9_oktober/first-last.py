# Vraag de gebruiker om een woord. Druk hiervan de eerste en de laatste letter af

word = input('Geef een woord in: ')

def firstLast(word):
    word = word.strip()
    return word[0], word[-1]

first, last = firstLast(word)

print(f'Eerste letter: {first}\nLaatste letter: {last}')