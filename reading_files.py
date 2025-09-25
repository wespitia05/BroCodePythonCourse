# python reading files (.txt, .json, .csv)

# ----- .txt ----- #
file_path = "output.txt"

try:
    with open (file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("that file was not found")
except PermissionError:
    print("you do not have permission to read that file")

# ----- .json ----- #
import json

file_path = "output.json"

try:
    with open (file_path, "r") as file:
        content = json.load(file)
        print(content)
        # access content with key
        print(content["name"])
        print(content["age"])
except FileNotFoundError:
    print("that file was not found")
except PermissionError:
    print("you do not have permission to read that file")

# ----- .csv ----- #
import csv
file_path = "output.csv"

try:
    with open (file_path, "r") as file:
        content = csv.reader(file)
        # without for loop to read each line, it will return memory address
        for line in content:
            print(line)
            # access an index
            print(line[1])    
            print(line[2])    
except FileNotFoundError:
    print("that file was not found")
except PermissionError:
    print("you do not have permission to read that file")