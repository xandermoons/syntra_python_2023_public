# Maak 2 lijsten aan, 1 met nummer en 1 met namen. Beide lijsten zijn even lang (5 items)
# Vul de lijst met nummers op van 1 tot en met 5
# Vul de lijst met namen op met 5 namen

nummers = [1,2,3,4,5, 6]
namen = ['Inias', 'Xander', 'Oliver', 'Ruben', 'Daan', 'Brecht']

print(f'Het eerste nummer in de lijst is: {nummers[0]}')
print(f'De eerste naam in de lijst is: {namen[0]}')

for i in range(1,min(len(nummers), len(namen))):
    print(f'Het volgende nummer in de lijst is: {nummers[i]}')
    print(f'De volgende naam in de lijst is: {namen[i]}')
    
# print ()

# for (nummer, naam) in zip(nummers, namen):
#     print(nummer)
#     print(naam)