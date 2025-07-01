# random numbers
import random

# low = 1
# high = 100
# options = ("rock", "paper", "scissors")
# cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# random whole integer (start,finish) range
# number = random.randint(low,high)

# returns random floating point number from 0-1
# number = random.random()

# choice method will randomly choose from given set of choices
# option = random.choice(options)

# shuffle method shuffles given list
# random.shuffle(cards)

# print (cards)

# ***** RANDOM NUMBER GUESSING GAME ***** #
low = 1
high = 100
guesses = 0
number = random.randint(low,high)

# escape while loop when you guess the number correctly
while True:
    # prompt user
    guess = int(input(f"Enter a number between {low} - {high}: "))
    # increment number of guesses
    guesses += 1

    if guess < number:
        print (f"{guess} is too low")
    elif guess > number:
        print (f"{guess} is too high")
    else:
        print (f"{guess} is correct!")
        break

print (f"This round took you {guesses} guesses")