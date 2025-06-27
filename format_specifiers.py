# format specifiers = {value:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use plus sign to indicate positive value
# := = palce sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator

price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

# :.2f rounds to two decimal points
print (f"Price 1 is ${price1:.2f}")
print (f"Price 2 is ${price2:.2f}")
print (f"Price 3 is ${price3:.2f}")

# allocate space, each value has a total of 10 spaces to display the output
print (f"Price 1 is ${price1:10}")
print (f"Price 2 is ${price2:10}")
print (f"Price 3 is ${price3:10}")

# left justify
print (f"Price 1 is ${price1:<10}")
print (f"Price 2 is ${price2:<10}")
print (f"Price 3 is ${price3:<10}")

# right justify
print (f"Price 1 is ${price1:>10}")
print (f"Price 2 is ${price2:>10}")
print (f"Price 3 is ${price3:>10}")

# indicate positive value
print (f"Price 1 is ${price1:+}")
print (f"Price 2 is ${price2:+}")
print (f"Price 3 is ${price3:+}")

# comma separator
print (f"Price 1 is ${price1:,}")
print (f"Price 2 is ${price2:,}")
print (f"Price 3 is ${price3:,}")

# postive, comma separator, 2 decimal points
print (f"Price 1 is ${price1:+,.2f}")
print (f"Price 2 is ${price2:+,.2f}")
print (f"Price 3 is ${price3:+,.2f}")