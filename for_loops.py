# for loops = execute a block of code a fixed number of times
# you can iterate over a range, string, sequence, etc

# for x in range of (start,finish)
# for x in range(1,11):
#     print(x)
# print ("END FOR LOOP")

# for x in reversed range of (start,finish)
# for x in reversed(range(1,11)):
#     print(x)
# print ("END FOR LOOP")

# for x in range of (start,finish,increment)
# for x in range(1,11,2):
#     print(x)
# print ("END FOR LOOP")

# for loop can print strings
# credit_card = "1234-5678-9012-3456"
# for x in credit_card:
#     print(x)

# print numbers from 1-20, skip 13
for x in range(1,21):
    if x == 13:
        continue
    else:
        print(x)