# reduce(function, collection): reduces elements in a collection to a single value
#                               for loop is better in most cases
#                               reduce is better for a functional approach + readability

from functools import reduce

# def add(x, y):
    # return x + y

prices = [19.99, 1.00, 5.75, 12.99, 10.99]

# x + y --> (x+y, y)
total = reduce(lambda x, y: x + y, prices)

print(f"${total}")