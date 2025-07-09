# Read a txt file and keep only one of the columns and nothing else, delimited by space
# cd D:\PythonProject\pythonscripts
# python .\txt2insertInto.py

def checkstring(somestring):
    match somestring.upper().rstrip('\n'):
        case "STRING":
            return 1
        case "INTEGER":
            return 2
        case _:
            return 3

# print out the select query with each cast column without the as statement
def insertInto(filename2): 
    total = "INSERT INTO " + wantAs + " VALUES ("
    with open(filename2, 'r') as txtfile:
        for row in txtfile:
            rowsplit = row.split(' ')
            if checkstring(rowsplit[1]) == 1:
                total += "'helloworld', "
            elif checkstring(rowsplit[1]) == 2:
                total += "1, "
            else:
                total += "NULL, "
        total += ");"
        print(total)

# get the csv file from the user, please note that the user only needs to type in the file name in the same directory and doesn't need to add in .csv suffix 
filename = input("Please enter the txt file name you want to convert to select SQL query: ")
filename = filename + ".txt"
print(filename)
wantAs = input("What table do you want to insert into?:   ").upper() # auto make it uppercase
insertInto(filename)
