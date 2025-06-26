import math

# basic arithmetic operators
friends = 10

# increment by 1, both give same result
# friends = friends + 1
# friends += 1

# decrement by 1, both give same result
# friends = friends - 1
# friends -= 1

# multiply, both give same answer
# friends = friends * 3
# friends *= 3

# divide, both give same answer
# friends = friends / 2
# friends /= 2

# exponent (squared), both give same answer
# friends = friends ** 2
# friends **= 2

# modulus (remainder)
# remainder = friends % 3

# built in math related functions
x = 3.14
y = 4
z = 5

# round to nearest whole number
# result = round(x)
# absolute value
# result = abs(y)
# power function, 4^3
# result = pow(4,3)
# maximum value
# result = max(x,y,z)
# minimum value
# result = min (x,y,z)

# print value of pi
print (math.pi)
# print value of e
print (math.e)
# square root
# result = math.sqrt(x)
# round up using ceil
# result = math.ceil(x)
# round down using floor
# result = math.floor(x)

# ***** EXAMPLES ***** #
# radius = float(input("Enter the radius of a circle: "))

# circumference = 2 * math.pi * radius

# print (f"The circumference is: {round(circumference, 2)}cm")


# radius = float(input("Enter the radius of a circle: "))

# area = math.pi * pow(radius,2)

# print (f"The area of the circle is: {round(area,2)}cm^2")


a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a,2) + pow(b,2))

print (f"Side C = {c}")