# default arguments = a default value for certain parameters
# default is used when that argument is omitted
# makes your functions more flexible, reduces # of arguments
# 1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary

# def net_price (list_price, discount = 0, tax = 0.05):
#     return list_price * (1 - discount) * (1 + tax)

# even with default arugments, you can still pass new ones to replace it
# print (net_price(500))
# print (net_price (500, 0.1))
# print (net_price (500, 0.1, 0))

import time

# when using default arguments, makes sure they are after any positional arguments
def count (end, start = 15):
    for x in range(start, end + 1):
        print(x)
        time.sleep(1)
    print ("DONE!")

count (30)