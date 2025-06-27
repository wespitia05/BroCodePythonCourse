# conditional expressions = one-line shortcut for the if-else statement (ternary operator)
# print or assign one of the two values based on a condition
# x if condition else y

num = 6
a = 6
b = 7
age = 13
temperature = 30
user_role = "admin"

# print ("Positive" if num > 0 else "Negative")
# modulus 2, is our number divisible by 2
# result = "EVEN" if num % 2 == 0 else "ODD"
# max_num = a if a > b else b
# min_num = a if a < b else b
# status = "Adult" if age >= 18 else "Child"
# weather = "HOT" if temperature > 20 else "COLD"
access_level = "Full Access" if user_role == "admin" else "Limited Access"

print (access_level)