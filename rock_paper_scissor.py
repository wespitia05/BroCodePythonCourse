# rock paper scissor game
import random

options = ("rock", "paper", "scissors")
running = True

while running:
    # reset the player
    player = None
    # reset the computer choice
    computer = random.choice(options)
    # while player input is not within the options the while loop will continue
    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print (f"Player: {player}")
    print (f"Computer: {computer}")

    if player == computer:
        print ("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print ("You win!")
    elif player == "paper" and computer == "rock":
        print ("You win!")
    elif player == "scissors" and computer == "paper":
        print ("You win!")
    else: 
        print ("You lose!")

    play_again = input("Play again? (Y/N): ").lower()
    # if player types something that is not y
    if not play_again == "y":
        running = False
print ("Thanks for playing!")