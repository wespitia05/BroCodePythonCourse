# dictionary = collection of {key:value} pairs ordered and changeable. NO duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# to get value from dictionary, get the key
# print (capitals.get("USA"))
# print (capitals.get("India"))
# print (capitals.get("Japan"))

# if capitals.get("Japan"):
#     print ("That capital exists")
# else:
#     print ("That capital doesn't exist")

# updating dictionary
# capitals.update ({"Germany": "Berlin"})
# print (capitals)

# change existing values
# capitals.update ({"USA": "Detroit"})

# remove key value pair with pop
# capitals.pop ("China")

# remove latest key value pair
# capitals.popitem()

# clears the dictionary
# capitals.clear()

# to get all keys within dictionary but not the values
# keys = capitals.keys()
# can iterate over them
# for key in capitals.key():
#     print (key)

# to get all values within dictionary but not the keys
# values = capitals.values()
# print (values)
# can iterate over them
# for value in capitals.values():
#     print (value)

# get both the key and value items
items = capitals.items()
for key, value in capitals.items():
    print (f"{key}: {value}")