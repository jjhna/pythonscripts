# Read a CSV file and print out the Select Query as a SQL, with the first line being the column name and the second line being the data type
# From the website: https://www.learnpython.org/en/Parsing_CSV_Files and https://stackoverflow.com/questions/14674275/skip-first-linefield-in-loop-using-csv-file and 
# cd D:\PythonProject\learnpython
# python .\excel2sql.py

# Note that the i is a string which is split into a list so that the contents can be printed out individually

import csv

# print out the select query with each cast column with the as statement
def withAs(filename2): 
    total = ""
    with open(filename2, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        total += "SELECT "
        for row in csvreader:
            for i in row: 
                splity = i.split()
                total += "CAST(\'" + splity[0] + "\' AS " + splity[1] + ") AS " + splity[0] + ", "
        print(total)

# print out the select query with each cast column without the as statement
def withoutAs(filename2): 
    total = ""
    with open(filename2, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        total += "SELECT "
        for row in csvreader:
            for i in row: 
                splity = i.split()
                total += "CAST(\'" + splity[0] + "\' AS " + splity[1] + "), "
        print(total)

"""
Note that this worked for another CSV file???

# print out the select query with each cast column with the as statement
def withAs(filename2): 
    total = ""
    with open(filename2, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        total += "SELECT "
        for row in csvreader:
            total += "CAST(\'" + row[0] + "\' AS " + row[1] + "), "
        print(total)

# print out the select query with each cast column without the as statement
def withoutAs(filename2): 
    total = ""
    with open(filename2, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        total += "SELECT "
        for row in csvreader:
            total += "CAST(\'" + row[0] + "\' AS " + row[1] + "), "
        print(total)

"""

# get the csv file from the user, please note that the user only needs to type in the file name in the same directory and doesn't need to add in .csv suffix 
filename = input("Please enter the csv file name you want to convert to select SQL query: ")
filename = filename + ".csv"
print(filename)
wantAs = input("Do you want AS statements added in? Y or N:   ").upper() # auto make it uppercase
if wantAs == 'Y':
    withAs(filename)
elif wantAs == 'N':
    withoutAs(filename)
else:
    print("You need to enter Y or N, please restart the app")



