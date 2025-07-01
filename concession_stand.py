# concession stand program

menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}

cart = []
total = 0

print ("---------- MENU ----------")
# prints out the menu
for key, value in menu.items():
    # key + 10 spaces, value to two decimal places
    print (f"{key:10}: ${value:.2f}")
print ("--------------------------")

# while user doesn't input "q"
while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    # if food from menu exists
    elif menu.get(food) is not None:
        # add food to cart, otherwise dont
        cart.append(food)

print ("------ YOUR ORDER ---------")
# for loop iterates through items in your cart
for food in cart:
    total += menu.get(food)
    print (food, end=" ")

print ()
print (f"Total is : ${total:.2f}")