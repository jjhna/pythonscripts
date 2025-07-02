# Read a txt file and print out the Select Query as a SQL, with the first line being the column name and the second line being the data type
# From the website: https://www.learnpython.org/en/Parsing_CSV_Files, see also csv2sql.py
# cd D:\PythonProject\pythonscripts
# python .\txt2sql.py

# strip() removes any trailing spaces or newline characters
# split() splits a string into a list of substrings, allowing iterations

# print out the select query with each cast column with the as statement
def withAs(filename2): 
    total = ""
    with open(filename2, 'r') as txtfile:
        next(txtfile)
        total += "SELECT "
        for row in txtfile:
            rowsplit = row.split(' ')
            stripnewline = rowsplit[1].strip()
            total += "CAST(\'" + rowsplit[0] + "\' AS " + stripnewline + ") AS " + rowsplit[0] + ", "
        print(total)

# print out the select query with each cast column without the as statement
def withoutAs(filename2): 
    total = ""
    with open(filename2, 'r') as txtfile:
        next(txtfile)
        total += "SELECT "
        for row in txtfile:
            rowsplit = row.split(' ')
            stripnewline = rowsplit[1].strip()
            total += "CAST(\'" + rowsplit[0] + "\' AS " + stripnewline + "), "
        print(total)

# get the csv file from the user, please note that the user only needs to type in the file name in the same directory and doesn't need to add in .csv suffix 
filename = input("Please enter the txt file name you want to convert to select SQL query: ")
filename = filename + ".txt"
print(filename)
wantAs = input("Do you want AS statements added in? Y or N:   ").upper() # auto make it uppercase
if wantAs == 'Y':
    withAs(filename)
elif wantAs == 'N':
    withoutAs(filename)
else:
    print("You need to enter Y or N, please restart the app")



