# Read a txt file and only keep certain rows that contain the certain keywords
# https://docs.liquibase.com/concepts/changelogs/xml-format.html
# cd D:\PythonProject\pythonscripts
# python .\readmultipletxt.py

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
    for i in filelist:
        filenamefull = "D:\\PythonProject\\SAMPLE_SERVER\\" + foldername + "\\" + i
        print(filenamefull)


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

    fileName = getListofFiles(filename, filename2)
    fileNameList = getListofFileNames(fileName)
    openfileList(filename, fileNameList)


if __name__ == "__main__":
    main()

        
'''
with open("newtext.sql", 'w') as file:
    file.write(total)
'''