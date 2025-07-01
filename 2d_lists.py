# 2D lists

# fruits = ["apple", "orange", "banana", "coconut"]
# vegetables = ["celery", "carrots", "potatoes"]
# meats = ["chicken", "fish", "turkey"]

# groceries = [fruits, vegetables, meats]

# print (groceries)
# index will be the list itself
# print (groceries[0]) # prints out fruits list
# [row] [column], 2nd row, second column
# print (groceries[2][2]) 

# nested loop to iterate over all elements
# for collection in groceries:
#     for food in collection:
#         print (food, end=" ")
#     print()

# ***** EXERCISE ***** #
num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

# for every row in num pad
for row in num_pad:
    # for every num in row (remove parenthesis)
    for num in row:
        print (num, end=" ")
    print() 