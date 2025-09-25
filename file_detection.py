# python file detection

# provides python programs to interact with operating systems
import os

# example of absolute file path: C:/Users/HP/Desktop/test.txt
file_path = "stuff/test.txt"

# access os module, then access path, then use built in method exists
# returns boolean value of true/false
if os.path.exists(file_path):
    print(f"the location '{file_path}' exists")

    # checks if file is in fact a file
    if os.path.isfile(file_path):
        print("that is a file")
    #checks if the directory is in fact a directory (aka a folder)
    elif os.path.isdir(file_path):
        print("that is a folder")
else:
    print("that location doesnt exist")