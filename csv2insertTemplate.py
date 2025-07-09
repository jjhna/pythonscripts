# Read a csv file and convert it into an insert statement
# cd D:\PythonProject\pythonscripts
# python .\csv2insertTemplate.py

import csv
import json

# print out the select query with each cast column with the as statement
def columnsplit(filename2, tableName2): 
    # total variable is what we will print out back to the user
    total = "\nINSERT INTO " + tableName2 + " ("
    with open(filename2, 'r', newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter='\t')

        # Iterates through each of the rows in the csv file
        for row in csvreader:
            rowKeys = row # Takes the value of the first row
            print(type(rowKeys))
            print(rowKeys)
            column0Split = row['Name'] # the contents of the columns under xxx
            column1Split = row['Age']
            column2Split = row['Sex']
            column3Split = row['Speicalpowa']
        
        # Takes the values of the first row and adds it to the total variable 
        for i in rowKeys:
            total += "'" + i + "', "
        total += ")\n" + "VALUES ("

        # Then we get the contents from the first 3 columns and add it to the total 
        total += "'" + column0Split + "','" + column1Split + "','" + column2Split + "',[\n"

        # For any columns that contain a JSON like variable will  be iterated through as a list and then inner looped through as a key value pair
        column3SingleLine = json.loads(column3Split) 
        for j in column3SingleLine:
            # print(f"Key: {item['Key']}, Value: {item['VALUE']}")
            for key, value in j.items():
                #print(f"Key: {key}, Value: {value}")
                if key == "Key":
                    total += "ARRAY('" + value
                else:
                    total += "','" + value + "'),\n"
        total += "],\n"
        total += "function1()\n"
        total += "function2());\n"
        print(total)

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
"""

# get the csv file from the user, please note that the user only needs to type in the file name in the same directory and doesn't need to add in .csv suffix 
filename = input("Please enter the csv file name you want to convert to select SQL query: ")
filename = filename + ".csv"
tableName = input("Please enter in both the DB and table name you want to insert into:   ")
columnsplit(filename, tableName)
#columnsplit("book1.csv", "aba")
