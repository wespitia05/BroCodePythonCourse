# sorting in python .sort() or .sorted()
# lists[], tuples[], dictionaries{"":""}, Objects

# --------- LISTS ----------- #
fruits = ["banana", "orange", "apple", "coconut"]

# fruits sorted in order
# fruits.sort()

# fruits sorted in reverse order
fruits.sort(reverse=True)

print (fruits)

# --------- TUPLES ----------- #
fruits = ("banana", "orange", "apple", "coconut")

# tuples dont have a sort() method
# cast it to a tuple to keep it as a tuple
# fruits = tuple(sorted(fruits))
# reverse order tuple
fruits = tuple(sorted(fruits, reverse=True))

print(fruits)

# --------- DICTIONARIES ----------- #
