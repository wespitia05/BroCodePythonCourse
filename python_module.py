# module = a file containing code you want to include in your program
# use 'import' to include module (built-in or your own)
# useful to break up a large program reusable separate files

import math
# you can import as an alias
# import math as m
# you can also import specific items
#from math import pi
#from math import e
# you can create your own module and import it in a differenct file
import module_example

# a,b,c,d,e = 1,2,3,4,5
# print (math.e ** a)
# print (math.e ** b)
# print (math.e ** c)
# print (math.e ** d)

result = module_example.pi
result = module_example.square(3)
result = module_example.cube(3)
result = module_example.circumference(3)
result = module_example.area(3)

print (result)