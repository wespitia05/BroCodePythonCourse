# dice roller
import random

# ● ┌ ─ ┐ │ └ ┘

"┌─────────┐"
"│         │"
"│    ●    │"
"│         │"
"└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

dice = []
total = 0
num_of_dice = int(input("How many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))

# this nested for loop displays them vertically
# outer for loop in charge of number of dice
# for die in range(num_of_dice):
    # inner for loop in charge of displaying the tuple
    # for line in dice_art.get(dice[die]):
    #     print (line)

# this for loop displays them horizontally
# outer loop iterates 5 times
for line in range(5):
    # inner loop displays them
    for die in dice:
        print (dice_art.get(die)[line], end="")
    print()
for die in dice:
    total += die

print (f"Total: {total}")