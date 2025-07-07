# iterables = an object/collection that can return its elements one at a time, allowing it to be iterated over in a loop

numbers = [1,2,3,4,5]
numbers1 = (1,2,3,4,5)

for number in numbers:
    print (number, end=" ")
for number in reversed(numbers):
    print (number, end=" ")

# for tuples
for number in numbers1:
    print (number, end=" ")
for number in reversed(numbers1):
    print (number, end=" ")

fruits = {"apples", "orange", "banana", "coconut"}

for fruit in fruits:
    print (fruit, end=" ")

name = "Bro Code"

for character in name:
    print (character, end="")

my_dictionary = {"A":1, "B":2, "C":3}
# returns key
for key in my_dictionary:
    print (key)
# returns value
for value in my_dictionary.values():
    print (value)
# returns both
for key, value in my_dictionary.items():
    # print (key, value)
    print (f"{key} = {value}")