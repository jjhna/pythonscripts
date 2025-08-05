# Read a txt file and only keep certain rows that contain the certain keywords
# https://docs.liquibase.com/concepts/changelogs/xml-format.html
# cd D:\PythonProject\pythonscripts
# python .\readmultipletxt2Script.py
# SAMPLE_DB_1

# function that reads the config.txt file to determine the folder name and the log files
def openAndGetFiles():
    ret = []
    with open("config.txt", 'r') as txtfile:
        aftersplit = []
        # split the row by spaces and strip any empty spaces before or after on each row and newlines and add them into a list
        for j in txtfile:
            aftersplit.append(j.strip().split(" "))
        # from the previous list, we will use the zip function to return our iteration as a tuple or paired item where we can get the 1st and 2nd top elements of each row back to the user
        for a, b in zip(aftersplit[0], aftersplit[1]):
            ret.append(a)
            ret.append(b)
    return ret

# function that removes all string instances, if it contains a special keyword 
def openAndripHype(filename):
    total = []
    #listofstuff = ["AGENTS.","AGENTO."] # list of strings you want to edit out, make sure its captialized 
    with open(filename, 'r') as txtfile:
        for j in txtfile:
            # Please note that the content below are taken from the readaftercertainkeywordstxt.py script, for more details please view that script instead
            if "--" not in j:
                total.append(j)
        return total

# function to open the source files list and scan through the files for the contents
# and find certain keywords in the text and append or add a string before that keyword
def openAndripDots(stringline):
    total = ""
    listofstuff = ["AGENTS.","AGENTO.","`AGENTS.","`AGENTO."] # list of strings you want to edit out, make sure its captialized 
    for j in stringline:
        # Please note that the content below are taken from the readaftercertainkeywordstxt.py script, for more details please view that script instead
        
        # note that strip also removes any leading or trailing whitelines and  \t, \n and \r
        stripped = j.strip()
        stripped2 = stripped.split()
        #print(stripped2)
        #if any(i in stripped2.upper() for i in listofstuff): # any() will return true if any of the iterable items are true, so the i is = to the s string and checks through the list for any related items
        #    print("hi")
        for i in stripped2:
            if any(j in i.upper() for j in listofstuff):
                beforestrip, afterstrip = i.split(".",1)
                total += "SERVER." + beforestrip + "." + afterstrip + " "
            elif i == stripped2[-1]: # if i the iteration is at the very last item in the list (stripped2[-1]) then we will add in a newline at the end
                total += i + "\n"
            else:
                #total += stripped + "\n"
                total += i + " "
    return total
    #with open(filename, 'w') as writefile:
    #    writefile.write(total)

def stripFiles(filelist):
    returnal = []
    for i in filelist:
        i.strip()
    for j in filelist:
        returnal = j.split("\n")
    if len(returnal) == 2:
        del returnal[1]
    elif len(returnal) % 2 != 0:
        del returnal[-1]
    print("returanl: ")
    print(returnal)
    return returnal

# function to return the list of files from the original text files
def getListofFiles(filename, filename2): 
    total = ""
    filenamefull = "D:\\PythonProject\\SAMPLE_SERVER\\" + filename + "\\LogFiles\\" + filename2
    #filenamefull = "D:\\PythonProject\\SAMPLE_SERVER\\SAMPLE_DB_1\\LogFiles\\SAMPLE_DB_1_LogFiles.xml"
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
    configList = openAndGetFiles()
    #filename = input("Please enter the folder name you want to utilize: ")
    for i in range(0, len(configList), 2):
        f1 = configList[i]
        f2 = configList[i+1]
        filename = f1
        filenametemp = "D:\\PythonProject\\SAMPLE_SERVER\\" + filename
        #print(filenametemp)
        #filename2 = input("Please enter the the Log file name you want to utilize: ")
        filename2 = f2 + ".xml"
        filenametemp = filenametemp + "\\LogFiles\\" + filename2
        print("filetemp " +filenametemp)
        print("\n")

        #issue in the getListofFiles()
        fullFileName = getListofFiles(filename, filename2)
        print("fullfile: " + fullFileName)
        fileNameList = getListofFileNames(fullFileName)
        print("filenamelist: ")
        print(fileNameList)
        returnal = stripFiles(fileNameList)
        fileNameTotalList = openfileList(filename, returnal)
        print("filenametotallist: ")
        print(fileNameTotalList)
        for i in fileNameTotalList:
            print("Here are the files you want to edit: " + i + "\n")
            theString = openAndripHype(i)
            theFinalString = openAndripDots(theString)      
            print(theFinalString)
            print("\n")


if __name__ == "__main__":
    main()

        