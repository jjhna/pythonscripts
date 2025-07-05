# Read a csv file and convert it into an insert statement
# cd D:\PythonProject\pythonscripts
# python .\csv2insertTemplate.py

import csv
import json

# print out the select query with each cast column with the as statement
def columnsplit(filename2, tableName2): 
    total = "INSERT INTO " + tableName2 + " ("
    with open(filename2, 'r', newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter='\t')
        column3Split = ""
        for row in csvreader:
            column3Split = row['Speicalpowa']
        column3SingleLine = json.loads(column3Split)
        for j in column3SingleLine:
            #print(f"Key: {item['Key']}, Value: {item['VALUE']}")
            for key, value in j.items():
                print(f"Key: {key}, Value: {value}")


"""
        strippy = firstRow[0].split('\t')
        for i in range(0, len(strippy)):
            total += strippy[i] + ", "
        total += ")\n" + "VALUES (\n"
        secondRow = next(csvreader)
        strippy2 = secondRow[0].split('\t')
        total += strippy2[0] + ", "
        total += strippy2[1] + ", "
        total += strippy2[2] + ", "
        #total += strippy2[3]
        total += ""
        print(total)
"""

# get the csv file from the user, please note that the user only needs to type in the file name in the same directory and doesn't need to add in .csv suffix 
#filename = input("Please enter the csv file name you want to convert to select SQL query: ")
#filename = filename + ".csv"
#tableName = input("Please enter in both the DB and table name you want to insert into:   ")
#columnsplit(filename, tableName)
columnsplit("book1.csv", "aba")
