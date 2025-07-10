# python slot machine
import random

def spin_row():
    # list of symbols as strings
    symbols = ['🍒', '🍉', '🍋', '🛎️', '⭐️']

    # empty list of results
    results = []

    # for loop will iterate 3 times
    for symbol in range(3):
        # pick random choice from symbols and add them to empty list of results
        results.append(random.choice(symbols))
    return results
    # can also do this
    # return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    # prints row with separator
    print (" | ".join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🛎️':
            return bet * 10
        elif row[0] == '⭐️':
            return bet * 20
    return 0
    
def main():
    # starting balance
    balance = 100

    # welcome menu
    print ("*************************")
    print ("Welcome to Python Slots")
    print ("Symbols: 🍒 🍉 🍋 🛎️  ⭐️")
    print ("*************************")

    # while the balance is greater than 0
    while balance > 0:
        # display current balance
        print (f"Current balance: ${balance}")

        # prompt user to input amount to bet
        bet = input("Place your bet amount: ")

        # if input is not a digit, display error message
        if not bet.isdigit():
            print ("Please enter a valid number")
            continue
        
        # type case input into an integer
        bet = int(bet)

        # check if bet is greater than balance, then print error message
        if bet > balance:
            print ("Insufficient funds")
            continue
        
        # check if bet is negative amount, then print error message
        if bet <= 0:
            print ("Bet must be greater than 0")
            continue
        
        # subtract bet from balance
        balance -= bet

        # row will be a list of random symbols
        row = spin_row()
        print ("Spinning...\n")
        print_row(row)
        # payout will be what we win
        payout = get_payout(row, bet)
        if payout > 0:
            print (f"You won ${payout}")
        else:
            print ("Sorry you lost this round")

        balance += payout

        play_again = input("Do you want to spin again? (Y/N): ").upper()

        if play_again != 'Y':
            break
    print ("************************************")
    print (f"Game over! Your final balance is ${balance}")
    print ("************************************")

if __name__ == '__main__':
    main()