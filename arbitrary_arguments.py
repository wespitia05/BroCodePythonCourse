# *args = allows you to pass multiple non-key arguments
# *kwargs = allows you to pass multiple keyword-arguments
# * unpacking operator
# 1. positional, 2. default, 3. keyword, 4. ARBITRARY

# pack arguments into a tuple
def add (*args):
    total = 0
    for arg in args:
        total += arg
    return total

# can put in as many arguments
# print (add(1,2,3))

def display_name (*args):
    for arg in args:
        print (arg, end=" ")
    
# display_name("Dr.", "Spongebob", "Harold", "Squarepants")

# ***** KEYWORD ARGUMENTS ***** #

def print_address (**kwargs):
    # prints every value
    for value in kwargs.values():
        print (value)
    # prints every key
    for key in kwargs.keys():
        print (key)
    # prints both
    for key, value in kwargs.items():
        print (f"{key}: {value}")

# print_address(street="123 Fake St.",
#               apt = "100",
#               city="Detroit", 
#               state="MI", 
#               zip="54321")

def shipping_label (*args, **kwargs):
    # for arg in args:
    #     print(arg, end=" ")
    # print()
    # for value in kwargs.values():
    #     print(value, end=" ")
    # kwargs.get retrieves value for the key specified
    if "apt" in kwargs:
        print (f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print (f"{kwargs.get('street')}")
        print (f"{kwargs.get('pobox')}")
    else:
        print (f"{kwargs.get('street')}")
    print (f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")


shipping_label("Dr.", "Spongebob", "Squarepants", "III", 
               street="123 Fake St.",
               pobox="PO Box #1001",
               city="Detroit",
               state="MI",
               zip="54321")