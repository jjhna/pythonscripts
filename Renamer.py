# Script to rename files
# From the website: https://learn.microsoft.com/en-us/windows/python/scripting
# cd D:\PythonProject\pythonscripts
# python .\Renamer.py


#import datetime
import os

# .. means up one directory and so the results will point to something like this: '..\\test_folder'
# note for a nested structure you would use something like: root = os.path.join('..', 'folder1', 'folder2', 'folder3')
root = os.path.join('..', 'test_folder')

for directory, subdir_list, file_list in os.walk(root):
    for name in file_list:
        # maps the path of the current directory with the name of the file in the entire file list
        source_name = os.path.join(directory, name)
        #timestamp = os.path.getmtime(source_name)
        #modified_date = str(datetime.datetime.fromtimestamp(timestamp)).replace(':','.')
        
        # joins the the os path with the word testing_ prefix in front of it
        target_name = os.path.join(directory, f'testing_{name}')

        print(f"Directory: {directory}")
        print(f"Subdirectories: {subdir_list}")
        print(f"Files: {file_list}")
        print(f'Renaming: {source_name} to: {target_name}')

        # built in os function rename which will rename the source_name to the target_name
        os.rename(source_name, target_name)

#PS D:\PythonProject\pythonscripts> python .\Renamer.py
#Renaming: ..\test_folder\testy1.txt to: ..\test_folder\testing_testy1.txt
#Renaming: ..\test_folder\testy2.txt to: ..\test_folder\testing_testy2.txt
#Renaming: ..\test_folder\testy3.txt to: ..\test_folder\testing_testy3.txt