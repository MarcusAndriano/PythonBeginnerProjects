import json
import csv

file_path = "/Users/marcusandriano/Desktop/Desktop cleanup/output.csv"

try:
    with open(file = file_path, mode = "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("You do not have permission to read file")
except KeyError:
    print(f"Could not find in file")