# Read a txt file and remove a certain keyword from the rows in the text file
# cd D:\PythonProject\pythonscripts
# python .\txt2remove.py

# print out the select query with each cast column without the as statement
def copytextfile(filename2): 
    total = ""
    with open(filename2, 'r') as txtfile:
        for row in txtfile:
            rowsplit = row.split(' ')
            for i in rowsplit:
                if "int" in i: # if keyword in the string then proceed to remove it
                    if "\n" in i: # if new line then we remove the keyword and add a newline, otherwise just an empty space
                        total += "\n"
                    else:
                        total += " "
                else:
                    total += i + " " # otherwise we add in the rest of the text file into the total variable
        print(total)
        with open("newtext.txt", 'w') as file:
            file.write(total)

# get the csv file from the user, please note that the user only needs to type in the file name in the same directory and doesn't need to add in .csv suffix 
filename = input("Please enter the txt file name you want to convert to select SQL query: ")
filename = filename + ".txt"
print(filename)
copytextfile(filename)
