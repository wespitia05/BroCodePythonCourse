# python writing files (.txt, .json, .csv)

# ----- .txt ----- #
# txt_data = "i like pizza"
employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]

# /Users/william/Desktop/output.txt is an absolute path
# output.txt is a relative path
file_path = "output.txt"

# with opens and closes file function
# open will return file object
# first parameter is file path, second is mode
# w = write, x = write (if file exists), a = append, r = read
try:
    with open(file=file_path, mode="w") as file: # file is name of file object
        # file.write(txt_data)
        # append data with new line
        # file.write("\n" + txt_data)
        # adding list to an empty file
        for employee in employees:
            file.write(employee + "\n")
        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("that file already exists")

# ----- .json ----- #
import json

employee = {
    "name": "Spongebob",
    "age": 30,
    "job": "Frycook"
}

file_path = "output.json"

try:
    with open(file_path, "w") as file:
        json.dump(employee, file, indent=4)
        print(f"json file '{file_path}' was created")
except FileExistsError:
    print("that file already exists")

# ----- .csv ----- #
# comma separated values
import csv

employees = [
    ["Name", "Age", "Job"], 
    ["Spongebob", 30, "Frycook"], 
    ["Patrick", 37, "Unemployed"], 
    ["Sandy", 27, "Scientist"]]

file_path = "output.csv"

try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print("that file already exists")