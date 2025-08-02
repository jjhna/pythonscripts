# Read a txt file and only keep certain rows that contain the certain keywords
# https://docs.liquibase.com/concepts/changelogs/xml-format.html
# cd D:\PythonProject\pythonscripts
# python .\readmultipletxt.py
# SAMPLE_DB_1

# function to open the source files list and scan through the files for the contents
def openAndripFiles(filelist):
    total = ""
    for i in filelist:
        with open(i, 'r') as txtfile:
            kickoff = False
            for j in txtfile:
                # Please note that the content below are taken from the readaftercertainkeywordstxt.py script, for more details please view that script instead

                # note that strip also removes any leading or trailing whitelines and  \t, \n and \r
                stripped = j.strip()
                #if stripped.startswith("WORKING_AREA"): #once we meet this keyword we can start saving the values
                #    kickoff = True
                
                # This is a better method, since we know the keyword is unique we just need to pull a partial pull from the list and from there make the kickoff turn True
                if "--changeset" in stripped:
                    kickoff = True
                # this should be first because if ) comes after the comma , py will skip over the else if statement below
                elif stripped.startswith("--comment") and kickoff == True:
                    total += prev + "\n"
                # we make sure to keep the previous iteration if we meet the ")" marker
                prev = stripped
    print(total)

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
    openAndripFiles(fileNameTotalList)


if __name__ == "__main__":
    main()

        
'''
with open("newtext.sql", 'w') as file:
    file.write(total)
'''