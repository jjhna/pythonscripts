# Read a txt file and only keep certain rows that contain the certain keywords, in this case rollback
# https://docs.liquibase.com/workflows/liquibase-community/using-rollback.html
# cd D:\PythonProject\pythonscripts
# python .\readmultipletxt2Roll.py
# SAMPLE_DB_1

# function that removes all string instances, if it contains a special keyword 
def openAndripHype(filename):
    total = []
    #listofstuff = ["AGENTS.","AGENTO."] # list of strings you want to edit out, make sure its captialized 
    with open(filename, 'r') as txtfile:
        for j in txtfile:
            # Please note that the content below are taken from the readaftercertainkeywordstxt.py script, for more details please view that script instead
            if "--rollback" in j:
                total.append(j)
        return total

# function to open the source files list and scan through the files for the contents
# and find certain keywords in the text and remove them from the text and return the rest to the user
def openAndripDash(stringline):
    total = ""
    for j in stringline:
        # Please note that the content below are taken from the readaftercertainkeywordstxt.py script, for more details please view that script instead
        
        # note that strip also removes any leading or trailing whitelines and  \t, \n and \r
        stripped = j.strip()
        stripped2 = stripped.split()
        #print(stripped2)
        for i in stripped2[1:]:
            if i == stripped2[-1]: # if i the iteration is at the very last item in the list (stripped2[-1]) then we will add in a newline at the end
                total += i + "\n"
            else:
                total += i + " "
    return total
    #with open(filename, 'w') as writefile:
    #    writefile.write(total)

# function to return the list of files from the original text files
def getListofFiles(filename, filename2): 
    total = ""
    #filenamefull = "D:\\PythonProject\\SAMPLE_SERVER\\" + filename + "\\LogFiles\\" + filename2
    filenamefull = "D:\\PythonProject\\SAMPLE_SERVER\\SAMPLE_DB_1\\LogFiles\\SAMPLE_DB_1_LogFiles.xml"
    with open(filenamefull, 'r') as txtfile:
        bodycount = 0
        for row in txtfile:
            rowsplit = row.split(' ')
            for s in rowsplit:
                if s == "<body>\n":
                    bodycount = 1
                elif (s == "</body>\n") and (bodycount == 1):
                    bodycount = 0
                elif bodycount == 1:
                    total += s
    return total

# function to return only the specific names of the files from the list of files
def getListofFileNames(totalFiles):
    totalList = []
    invalidwords = ["<", "/>"]
    totalFiles = totalFiles.split('"')
    for row in totalFiles:
       if all(e not in row for e in invalidwords):
           row = row.replace("/", "\\")
           totalList.append(row)
    return totalList

# function to open the list of files to get the table names
def openfileList(foldername, filelist):
    total = []
    for i in filelist:
        filenamefull = "D:\\PythonProject\\SAMPLE_SERVER\\" + foldername + "\\" + i
        total.append(filenamefull)
    return total 


def main():
    # get the csv file from the user, please note that the user only needs to type in the file name in the same directory and doesn't need to add in .csv suffix 
    fileName = ""
    fileNameList = []
    filename = input("Please enter the folder name you want to utilize: ")
    filenametemp = "D:\\PythonProject\\SAMPLE_SERVER\\" + filename
    print(filenametemp)
    filename2 = input("Please enter the the Log file name you want to utilize: ")
    filename2 = filename2 + ".xml"
    filenametemp = filenametemp + "\\LogFiles\\" + filename2
    print(filenametemp)
    print("\n")

    fileName = getListofFiles(filename, filename2)
    fileNameList = getListofFileNames(fileName)
    fileNameTotalList = openfileList(filename, fileNameList)
    theString = ""
    theFinalString = ""
    for i in fileNameTotalList:
        print("Here are the files you want to edit: " + i + "\n")
        theString = openAndripHype(i)
        theFinalString = openAndripDash(theString)      
        print(theFinalString)
        print("\n")


if __name__ == "__main__":
    main()

        