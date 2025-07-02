# collections = single "variable" used to store multiple values
# list = [] ordered and changeable. duplicates are OK
# set = {} unordered and immutable, but add/remove ok. NO duplicates
# tuples = () ordered and unchangeable, duplicates OK. FASTER

# lists
fruits = ["apple", "orange", "banana", "coconut"]
# print (fruits)
# print (fruits[0]) # index 0
# print (fruits[1]) # index 1
# print (fruits[2]) # index 2
# print (fruits[0:3]) # first 3
# print (fruits[:3]) # first 3
# print (fruits[::2]) # every 2nd element
# print (fruits[::-1]) # reversed

# print all using for loop
for fruit in fruits:
    print (fruit)

# print length of list
print (len(fruits))

# find out if value is in a list
print ("apple" in fruits)

# change values at certain indexes
# fruits[0] = "pineapple"
# for fruit in fruits:
#     print (fruit)

# append an element (add to end of list)
fruits.append("pineapple")
print (fruits)

# remove an element
fruits.remove("apple")
print (fruits)

# insert an element
fruits.insert(0, "pineapple")
print (fruits)

# sort the list
fruits.sort()
print (fruits)

# reverse the list
fruits.reverse()
print (fruits)

# reverse in alphabetical order
fruits.sort()
fruits.reverse()
print (fruits)

# clear a list
# fruits.clear()
# print (fruits)

# return index of a value
print (fruits.index("banana"))

# return count of an element
print (fruits.count("banana"))

# sets
fruits = {"apple", "orange", "banana", "coconut"}
print (fruits)

# add elements
fruits.add("pineapple")

# remove elements
fruits.remove("apple")

# remove whatever element is first (random)
fruits.pop()

# tuples
fruits = ("apple", "orange", "banana", "coconut", "pineapple")
print (fruits)

# find index of element
print (fruits.index("apple"))

# count number of elements in tuple
print (fruits.count("coconut"))