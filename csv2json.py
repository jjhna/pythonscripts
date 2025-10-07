# Test csv to json converter
# cd D:\PythonProject\pythonscripts
# python .\csv2json.py

import csv
import json

with open("dbz.csv", 'r', newline='') as csvopen:
    csvopen2 = csv.DictReader(csvopen, delimiter=',')
    printstatement = ""

    for i in csvopen2:
        c1 = i['ID']
        c2 = i['Name']
        printstatement = "{ ID: " + c1 + " Name: " + c2 + " }"

        jsonstring = json.dumps(printstatement, indent=4)
        print(jsonstring)
