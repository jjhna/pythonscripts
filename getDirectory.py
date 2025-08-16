# Read a txt file and only keep certain rows that contain the certain keywords
# cd D:\PythonProject\pythonscripts
# python .\getDirectory.py

import os

total = ""
directoryvar = input("What directory do you want to pull up all the folders: ")

for i in os.listdir(directoryvar):
    total += i + "\n"

with open("directorytxt.sql", 'w') as file:
    file.write(total)
