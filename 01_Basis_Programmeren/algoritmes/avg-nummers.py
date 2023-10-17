# bereken het gemiddelde van x aantal nummers

nummers = []

while True:
    nr = input('Geef een nummer in. Als alle nummers ingegeven zijn schrijf dan "STOP": ')
    if nr == 'STOP':
        break
    nr = int(nr)
    nummers.append(nr)

print(f'Het gemiddelde is: {sum(nummers)/len(nummers)}')