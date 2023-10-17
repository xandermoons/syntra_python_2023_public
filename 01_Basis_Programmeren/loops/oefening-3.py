# Vraag de gebruiker om een tekst in te geven. Tel het aantal letters en cijfers en druk deze dan af

text = input('Geef een tekst met letters en cijfers in: ')

letters = []
cijfers = []

for chr in text:
    if chr.isalpha():
        letters.append(chr)
    if chr.isdigit():
        cijfers.append(chr)

print(f'Er zijn {len(letters)} letters gevonden: {" ".join(letters)}\nEr zijn {len(cijfers)} cijfers gevondena: {" ".join(cijfers)}')