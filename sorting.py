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
fruits = {"banana": 105,
          "orange": 73,
          "apple":72,
          "coconut": 354}

# items method will return each pair as a tuple
# wrap in dict method to return dictionary
# fruits = dict(sorted(fruits.items()))

# reverse order
# fruits = dict(sorted(fruits.items(), key=lambda item: item[0], reverse=True))

# sort dictionary by value
# fruits = dict(sorted(fruits.items(), key=lambda item: item[1]))
# sort dictionary in reverse by value
fruits = dict(sorted(fruits.items(), key=lambda item: item[1], reverse=True))

print(fruits)

# --------- OBJECT ----------- #
class Fruit:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories
    
    def __repr__(self):
        return f"{self.name}: {self.calories}"
    
fruits = [Fruit("banana", 105),
          Fruit("apple", 72),
          Fruit("orange", 73),
          Fruit("coconut", 354)]

# sorted in alphabetical order
# fruits = sorted(fruits, key=lambda fruit:fruit.name)

# sorted in reverse alphabetical order
# fruits = sorted(fruits, key=lambda fruit:fruit.name, reverse=True)

# sorted by value
# fruits = sorted(fruits, key=lambda fruit:fruit.calories)

# sorted by reverse value
fruits = sorted(fruits, key=lambda fruit:fruit.calories, reverse=True)

print(fruits)