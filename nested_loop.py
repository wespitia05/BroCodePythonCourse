# nested loop = a loop within another loop (outer,inner)
# outer loop:
#   inner loop:

# repeat it 3 times
# for x in range(3):
#     for y in range(1, 10):
#         # end="" prints in the same line, no space
#         # end=" " prints in the same line, spaces
#         print(y, end="")
#     print()

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to use: ")

# outer loop in charge of the rows
for x in range(rows):
    # inner loop in charge of the columns
    for y in range(columns):
        print(symbol, end="")
    print()