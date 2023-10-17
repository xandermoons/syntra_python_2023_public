# Vraag de gebruiker om een woord of zin en geef weer hoeveel letters er in dit woord zitten

zin = input('Geef een woord in: ')

def lengte_van_zin(zin):
    woorden = zin.split(' ')
    res = 0
    for woord in woorden:
        res += len(woord)
    return res

print(lengte_van_zin(zin))