# Read a csv file and keep only one of the columns and nothing else, delimited by space
# cd D:\PythonProject\pythonscripts
# python .\csv2column.py

import csv

# print out the select query with each cast column with the as statement
def columnsplit(filename2, columnchoice): 
    total = ""
    with open(filename2, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            for i in row: 
                splity = i.split()
                total += splity[columnchoice] + "\n"
        print(total)

# get the csv file from the user, please note that the user only needs to type in the file name in the same directory and doesn't need to add in .csv suffix 
filename = input("Please enter the txt file name you want to convert to select SQL query: ")
filename = filename + ".csv"
columnsplit(filename)

# get the csv file from the user, please note that the user only needs to type in the file name in the same directory and doesn't need to add in .csv suffix 
filename = input("Please enter the txt file name you want to convert to select SQL query: ")
filename = filename + ".csv"
print(filename)
wantAs = input("Which column do you want to choose:   ") 
wantAs2 = wantAs.isdigit()
if wantAs2 == True:
    columnsplit(filename, wantAs)
else:
    print("You need to enter a digit please restart the app")

