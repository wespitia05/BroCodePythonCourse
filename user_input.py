# user input

# displays msg, doesn't continue until user enters a value
# name = input ("Enter your name: ")
# age = input ("Enter your age: ")
# age = int(age) # need this bc age is a string at first in the input
# # could also do int(input())
# age = age + 1

# print (f"Hello {name}")
# print (f"You are {age} years old")

# ***** MAD LIBS ***** #
# adjective1 = input ("Enter an adjective: ")
# noun = input ("Enter a noun: ")
# adjective2 = input ("Enter an adjective: ")
# verb = input ("Enter a verb: ")
# adjective3 = input ("Enter an adjective: ")

# print (f"Today I went to a {adjective1} zoo.")
# print (f"In an exhibit, I saw {noun}.")
# print (f"{noun} was {adjective2} and {verb}ing")
# print (f"I was {adjective3}.")

# ***** AREA/VOLUME CALC ***** #
# length = float(input ("Enter the length of a rectangle: "))
# width = float(input ("Enter the width of a rectangle: "))
# height = float(input ("Enter the height of a rectangle: "))

# area = length * width
# volume = length * width * height

# print (f"The area is {area}cm^2")
# print (f"The volume is {volume}cm^3")

item = input ("What item would you like to buy?: ")
price = float(input ("What is the price?: "))
quantity = int(input ("How many would you like?: "))

total = price * quantity

print (f"You have bought {quantity} x {item}/s")
# round (total, # of decimal places)
print (f"Your total is: ${round(total, 2)}")