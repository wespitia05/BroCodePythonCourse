# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

# ***** LOCAL ***** #
# def func1():
#     a = 1
#     print (a) # cannot be b

# def func2():
#     b = 2
#     print (b) # cannot be a

# func1()
# func2()

# ***** GLOBAL ***** #
# def func1():
#     print(x)

# def func2():
#     print(x)

# x = 3

# func1()
# func2()

# ***** BUILT-IN ***** #
from math import e

def func1():
    print(e)

e = 3 # would print out global version instead

func1()