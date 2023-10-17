# Lees deze file in een nieuw programma en toon alle personen en hun leeftijd. Toon ook wie de oudste en de jongste is.

import json
import csv

persons = []

def read_json():
    with open("02_Python_Basis/json/names.json", 'r') as f:
        global persons
        persons = json.load(f)

def find_oldest():
    ages = list()
    for person in persons:
        ages.append(int(person['leeftijd']))
    return max(ages), min(ages)

def read_csv():
    with open("02_Python_Basis/json/names.csv", 'r') as f:
        csvreader = csv.reader(f, delimiter=',')
        for row in csvreader:
            persons.append({'name' : row[0], 'age' : row[1]})

def main():
    read_csv()
    print(persons)

main()