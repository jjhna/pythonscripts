# Read an excel file and convert that into an xml file
# cd D:\PythonProject\pythonscripts
# python .\excel2xml.py

import csv
# xml etree is a tool that creates XML files for the user
# it requires one root element because XML's are a tree structure
# each of the tags in an XML is considered an element, hence element tree
import xml.etree.ElementTree as ET

with open('test.csv', 'r') as csvfile:
    csvfileread = csv.DictReader(csvfile)

    # Creates the root element People as the first element in the XML tree
    root = ET.Element('People')

    for row in csvfileread:
        # creates each other element as Person in the XML tree
        person = ET.SubElement(root, 'Person')
        for key, value in row.items():
            # so stuff like key would be the column header which would either be ID, Name, Age, etc
            # and then the person would be the Person element mentioned above so each entry will be attached to its own Person Element in the tree
            child = ET.SubElement(person, key)
            # value would be the value of the key for that particular entry so if ID is 1 then 1 would be the value or Name is Bob then Bob = value
            child.text = value

tree = ET.ElementTree(root)
# adds this to the very first line of the xml file: <?xml version='1.0' encoding='utf-8'?>
tree.write('result.xml', encoding='utf-8', xml_declaration=True)


print("results will be in result.xml")
