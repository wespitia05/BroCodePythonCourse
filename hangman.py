# hangman in python
import random

# we'll need a set of words chosen at random
words = ("apple", "orange", "banana", "coconut", "pineapple")

# dictionary of key:()
hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/  "),
               6: (" o ",
                   "/|\\",
                   "/ \\")}

def display_hangman(wrong_guesses):
    print("******************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("******************")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    # choose random answer from list of words
    answer = random.choice(words)
    # blanks multiplied by length of random word chosen
    hint = ["_"] * len(answer)
    # keep track of wrong guesses
    wrong_guesses = 0
    # keep track of guessed letters
    guessed_letters = set()
    # while our game is running, keep going
    is_running = True

    while is_running:
        display_hangman(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed")

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else: 
            wrong_guesses += 1
        
        if "_" not in hint:
            display_hangman(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_hangman(wrong_guesses)
            display_answer(answer)
            print ("YOU LOSE!")
            is_running = False

if __name__ == "__main__":
    main()