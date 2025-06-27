# name = input("Enter your full name: ")
# phone_number = input("Enter your phone number: ")

# len() gives us length of the string
# result = len(name)
# find() method returns first occurance of given character
# rfind() method returns last occurance of given character
# result = name.find(" ")
# result = name.rfind("o")
# capitalize() method will capitalize the first letter of the given string
# name = name.capitalize()
# upper() method will capitalize the entire string
# name = name.upper()
# lower() method will lowercase the entire string
# name = name.lower()
# isdigit() will tell us true/false if given string has only digits 
# result = name.isdigit()
# isalpha() returns true/false if string contains only alphabetical letters (no spaces)
# result = name.isalpha()
# count() returns how many characters are in a given string
# result = phone_number.count("-")
# replace() takes first character given and replaces it with second given character
# result = phone_number.replace("-", " ")

# print (result)


# ***** EXERCISE ***** #
# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter a username: ")

username.find(" ")

# if username is greater than 12 characters
if len(username) > 12:
    print("Your username cannot be more than 12 characters")
# if result is not -1, meaning we found a space
elif not username.find(" ") == -1:
    print ("Your username cannot contain spaces")
# if username contains numbers
elif not username.isalpha():
    print ("Your username cannot contain numbers")
else: 
    print (f"Welcome {username}")