# typecasting is the process of converting a value of one data type to another
# (string, integer, float, boolean)
# explicit vs implicit

# ***** EXPLICIT ***** #
name = "Bro" # string
age = 21 # integer
gpa = 1.9 # float
student = True # boolean

# type prints out data type
print (type(name))
print (type(age))
print (type(gpa))
print (type(student))

# convert age to a float
age = float(age)
print (age)
print (type(age))

# convert gpa to an integer
gpa = int(gpa)
print (gpa)
print (type(gpa))

# convert student to a string
student = str(student)
print (student)
print (type(student))

# convert age to boolean
# if number is anything but 0, will be true
# if string is empty, will be false
age = bool(age)
print (age)
print (type(age))

# ***** IMPLICIT ***** #
x = 2
y = 2.0

x = x / y

# integer / float, answer is a float
print (x)