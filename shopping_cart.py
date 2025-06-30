# shopping cart program

# not using tuples bc they are unchangeable
# not using sets bc they are unordered
foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    # .lower() takes input and turns it into lowercase
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print ("----- YOUR CART -----")

for food in foods:
    # end=" " prints in same line
    print (food, end=" ")

for price in prices:
    total += price

print()
print (f"Your total is: ${total}")