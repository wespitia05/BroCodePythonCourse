# exception: an event that interrupts the flow of a program
#            (ZeroDivisionError, TypeError, ValueError)
#            1.try, 2.except, 3.finally

# gives us value error
# int("pizza") 

# number = int(input("enter a number: "))
# if you type in 0, you get the zero division error
# if you type a word, you get a value error
# print(1 / number)

try:
    number = int(input("enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("you cannot divide by zero, idiot")
except ValueError:
    print("enter only numbers please")
except Exception: # handles ALL errors
    print("something went wrong")
finally: # always executes even if there is an exception or not
    print("do some cleanup here")