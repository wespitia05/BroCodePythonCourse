# varaible is a container for a value (string, integer, float, boolean)
# a variable behaves as if it was the value it contains

# strings
first_name = "Bro"
food = "pizza"
email = "Bro123@fake.com"

print (f"Hello {first_name}")
print (f"You like {food}")
print (f"Your email is: {email}")

#integers
age = 25
quantity = 3
num_of_students = 30

print (f"You are {age} years old")
print (f"You are buying {quantity} items")
print (f"Your class has {num_of_students} students")

# floats
price = 10.99
gpa = 3.2
distance = 5.5

print (f"The price is ${price}")
print (f"your gpa is {gpa}")
print (f"You ran {distance}km")

# boolean
is_student = False
for_sale = False
is_online = True

print (f"Are you a student?: {is_student}")

if is_student:
    print ("You are a student")
else:
    print ("You are NOT a student")

if for_sale:
    print ("That item is for sale")
else:
    print ("That item is NOT available")

if is_online:
    print ("You are online")
else: 
    print ("You are offline")