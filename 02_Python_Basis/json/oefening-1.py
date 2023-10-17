# Vraag de gebruiker om een aantal namen en leeftijden. Van elke persoon houden we de naam bij en de leeftijd. Bewaar dit als een json file. Als formaat willen we zien "name:"..."age":...

# Bewaar dit nu ook als csv en lees dan ook die csv opnieuw in. 

# Neem een kopie van het eerste programma en wijzig de leeftijd naar geboortedatum. Bewaar dit dan ook als een json file

# Neem eem kopie vna het inleesprogramma en wijzig hier ook de leeftijd naar geboortedatum en lees de outpit van de file in en toon alles wat er in staat

import json
import csv

persons = list()

def voeg_toe():
    name = input('Geef de naam van de persoon in: ')
    age = input('Geef de leeftijd van deze persoon in: ')
    persons.append({'name' : name , 'age' : age})

def write_json():
    with open("02_Python_Basis/json/names.json", mode='w') as f:
        f.write(json.dumps(persons))

def write_csv():
    with open('02_Python_Basis/json/names.csv', 'w', newline='') as csvfile:
        w = csv.writer(csvfile, delimiter=',')
        for dictionary in persons:
            w.writerow(dictionary.values())

def main():
    for i in range(3):
        voeg_toe()
    print(persons)
    write_json()
    write_csv()

main()
