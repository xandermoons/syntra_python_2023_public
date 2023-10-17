# Vraag de gebruiker 5 maal een getal tussen 1 en 10. Hou deze bij in een lijst. 
# Na in gave toon dan alle getallen kleiner dan het ingegeven getal die deelbaar zijn door 3 
# en druk op het einde de lijst af van de ingegeven getallen.

getallen = []

# Een functie om te checken of de input van de gebruiker correct is
def check_getal(getal):
    if getal.isnumeric() == False:
        return False
    
    elif int(getal) < 1:
        return False
    
    elif int(getal) > 10:
        return False
    
    return True

# Deze lus vraagt 5 getallen aan de gebruiker. Als de lus gedaan is wordt deze geprint.
for i in range(5):

    getal = input('Geef een getal in tussen 1 en 10: ')

    while check_getal(getal) == False:
        getal = input('Fout! Geef een geldige waarde in tussen 1 en 10: ')
        
    getal = int(getal)
    getallen.append(getal)

    print(f'getallen deelbaar door 3 die kleiner zijn dan {getal}: ' , end='')

    # Deze lus gaat per ingegeven getal kijken of de getallen die kleiner zijn deelbaar zijn door 3. Zo ja worden ze geprint.
    for i in range(1, getal):
        
        if(i % 3 == 0):
            print(i , end='   ')
    print('')

print(f'Getallen: {getallen}')