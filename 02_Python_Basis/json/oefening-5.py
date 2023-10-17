# Neem eem kopie vna het inleesprogramma en wijzig hier ook de leeftijd naar geboortedatum en lees de outpit van de file in en toon alles wat er in staat

import json
import csv

persons = list()

def voeg_toe():
    name = input('Geef de naam van de persoon in: ')
    dob = input('Geef de geboortedatum van deze persoon in: ')
    persons.append({'name' : name , 'date of birth' : dob})

def write_json():
    with open("02_Python_Basis/json/names_dob.json", mode='w') as f:
        f.write(json.dumps(persons))

def write_csv():
    with open('02_Python_Basis/json/names_dob.csv', 'w', newline='') as csvfile:
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
