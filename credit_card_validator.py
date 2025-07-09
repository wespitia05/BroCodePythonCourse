# python credit card validator program

# 1. remove any '-' or ' '
# 2. add all digits in the odd places from right to left
# 3. double every second digit from right to left
# (if result is a two-digit number, add the two-digit number together to get a single digit)
# 4. sum the totals of steps 2 and 3
# 5. if sum is divisible by 10, the credit card # is valid

sum_odd_digits = 0
sum_even_digits = 0
total = 0

# Step 1
card_number = input("Enter a credit card number: ")
# removes an '-' in the input
card_number = card_number.replace("-", "")
# removes any ' 'in the input
card_number = card_number.replace(" ", "")
print(f"Your card number after removing items: {card_number}")

# Step 2
# reverse our string (makes it easier to add from right to left)
card_number = card_number[::-1]
print (f"Your card number reversed: {card_number}")
# iterate over every second digits
for x in card_number[::2]:
    sum_odd_digits += int(x) # typecast x as an integer

# Step 3
# doubles every second digit from right to left
for x in card_number[1::2]:
    x = int(x) * 2
    # check if x is a two digit number
    if x >= 10:
        # split that number, then add them tg
        # % 10 gives remainer of any digit
        # 9 * 2 = 18 
        # 18 % 10 = 8
        sum_even_digits += (1 + (x % 10))
    else: # means x must be less than 10
        sum_even_digits += x

# Step 4
total = sum_odd_digits + sum_even_digits
print (f"Total = {total}")

# Step 5
if total % 10 == 0:
    print("VALID")
else:
    print("INVALID")