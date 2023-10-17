import json
import csv
from datetime import date

persons = []

def read_json():
    with open("02_Python_Basis/json/names_dob.json", 'r') as f:
        global persons
        persons = json.load(f)

def find_oldest():
    dobs = list()
    for person in persons:
        day,month,year = person['date of birth'].split('/')
        dob = date(day=int(day), month=int(month), year=int(year))
        dobs.append(dob)
    return min(dobs), max(dobs)

def read_csv():
    with open("02_Python_Basis/json/names_dob.csv", 'r') as f:
        csvreader = csv.reader(f, delimiter=',')
        for row in csvreader:
            persons.append({'name' : row[0], 'date of birth' : row[1]})

def main():
    read_json()
    print(persons)
    read_csv()
    print(persons)
    print(find_oldest())

main()