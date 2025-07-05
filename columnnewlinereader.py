# Read a csv file and convert it into an insert statement
# cd D:\PythonProject\pythonscripts
# python .\columnnewlinereader.py

import csv
import json

with open('book2.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        raw_json = row['attributes']
        try:
            parsed = json.loads(raw_json)
            for item in parsed:
                print(f"Key: {item['Key']}, Value: {item['VALUE']}")
        except json.JSONDecodeError as e:
            print("Failed to parse JSON:", e)
            print("Raw JSON:", raw_json)