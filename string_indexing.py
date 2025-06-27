# indexing = accessing elements of a sequence using [] (indexing operator)
# [start : end : step]

credit_number = "1234-5678-9012-3456"

# get value of given index
print (credit_number[5])
# if we want first 4 digits
print (credit_number[0:4])
# if we want next set of digits
print (credit_number[5:9])
# if we want last 12 digits
print (credit_number[5:])
# if we want last character in a string
print (credit_number[-1])
# if we want second to last character in a string
print (credit_number[-2])
# if we want every second character in a string
print (credit_number[::2])
# if we want every third character in a string
print (credit_number[::3])
# if we want the last 4 digits of the string
print (credit_number[-4:])
print (f"XXXX-XXXX-XXXX-{credit_number[-4:]}")
# if we want to reverse a string
print (credit_number[::-1])