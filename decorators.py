# decorator: a function that extends the behavior of another function w/o modifying the base function
#   pass the base function as an argument to the decorator

#           @add_sprinkles
#           get_ice_cream("vailla")

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("you added sprinkles")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("you added fudge")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print("here is your {flavor} ice cream :)")

get_ice_cream("chocolate")