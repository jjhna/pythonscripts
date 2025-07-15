# Read a txt file and only keep certain rows that contain the certain keywords
# cd D:\PythonProject\pythonscripts
# python .\txt2keep.py

# print out the select query with each cast column without the as statement
def copytextfile(filename2): 
    total = ""
    with open(filename2, 'r') as txtfile:
        for row in txtfile:
            rowsplit = row.split(' ')
            listofstuff = ["INT","STRING"] # list of strings you want to edit out, make sure its captialized 
            for s in rowsplit:
                if any(i in s.upper() for i in listofstuff): # any() will return true if any of the iterable items are true, so the i is = to the s string and checks through the list for any related items
                    total += "sum " + s + " "
                else:
                    total += s + " "
        print(total)

# get the csv file from the user, please note that the user only needs to type in the file name in the same directory and doesn't need to add in .csv suffix 
filename = input("Please enter the txt file name you want to convert to select SQL query: ")
filename = filename + ".txt"
print(filename)
copytextfile(filename)
