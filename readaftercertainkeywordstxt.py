# Read a txt file and only keep certain rows after a certain keyword
# cd D:\PythonProject\pythonscripts
# python .\readaftercertainkeywordstxt.py

# function to return only the specific names of the files from the list of files
def getSQLcontents(filename):
    total = ""
    # Please note here that we added in a variable called kickoff to only trigger saving the strings from the list after meeting certain keywords
    kickoff = False
    with open(filename, 'r') as txtfile:
        for row in txtfile:
            # note that strip also removes any leading or trailing whitelines and  \t, \n and \r
            stripped = row.strip()
            if stripped.startswith("WORKING_AREA"): #once we meet this keyword we can start saving the values
                kickoff = True
            elif stripped.endswith(",") and kickoff == True: 
                total += stripped + "\n"
            elif stripped.startswith(")") and kickoff == True:
                total += prev
            # we make sure to keep the previous iteration if we meet the ")" marker
            prev = stripped
        return(total)


def getSQLline(strippedearlier):
    total = ""
    strippedintolines = strippedearlier.split('\n')
    for i in strippedintolines:
        i = i.split(' ')
        if i[0] != None:
            total += i[0] + "\n"
    return total

def oneSQLline(strippedcolumn):
    total = ""
    strip = strippedcolumn.split('\n')
    for i in strip[:-1]:
        total += i.upper() + ","
    return total

def ifExist(onestringlist):
    total = ""
    listofstuff = ["AGENT_NAME","COUNTRY"]
    for s in onestringlist:
        if any(i in s for i in listofstuff): # any() will return true if any of the iterable items are true, so the i is = to the s string and checks through the list for any related items
            total += "CAST " + s + " AS CHUMP,"
        else:
            total += s + ","
    return total

def createInsert(strippedline):
    total = "INSERT INTO DB.TABLE (COLUMN1) VALUES ( "
    checkline = strippedline.split(',')
    total += ifExist(checkline)
    total += " );"
    return total

def main():
    # get the csv file from the user, please note that the user only needs to type in the file name in the same directory and doesn't need to add in .csv suffix 
    #filename = input("Please enter the file name you want to utilize: ")
    #filename += ".sql"
    filename = "SAMPLE_TABLE_1.sql"
    strippedresults = getSQLcontents(filename)
    #print(strippedresults)
    strippedcolumns = getSQLline(strippedresults)
    strippedoneline = oneSQLline(strippedcolumns)
    strippedlineInsert = createInsert(strippedoneline)
    print(strippedlineInsert)

if __name__ == "__main__":
    main()

        
'''
with open("newtext.sql", 'w') as file:
    file.write(total)
'''
