# logical operators = used on conditional statements
# and = checks two or more conditions is True
# or = checks if at least one condition is True
# not = True if condition is False, and vice versa

temp = 40
sunny = True

# if temp > 0 and temp < 30:
#     print ("The temperature is good")
# else: 
#     print ("The temperature is bad")

if temp <= 0 or temp >= 30:
    print ("The temperature is good")
else: 
    print ("The temperature is bad")

if not sunny:
    print ("It is cloudy outside")
else:
    print ("It is sunny outside")