import random

options = ("rock", "paper", "scissors")
running = True

while running:

    gamer = None
    device = random.choice(options)

    while gamer not in options:
        gamer = input("Enter a choice (rock, paper, scissors): ")

    print(f"Gamer: {gamer}")
    print(f"Your PC: {device}")

    if gamer == device:
        print("It's a tie!")
    elif gamer == "rock" and device == "scissors":
        print("HURRAY!!!You won!")
    elif gamer == "paper" and device == "rock":
        print("HURRAY!!!You won!")
    elif gamer == "scissors" and device == "paper":
        print("HURRAY!!!You won!")
    else:
        print("OOPS!!!You lose!")

    if not input("Wanna play again? (y/n): ").lower() == "y":
        running = False

print("Thanks for playing!")
