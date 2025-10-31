import random
options = ("rock", "paper", "scissor")

player = None
computer = random.choice(options)
play = True

player = input("Enter your choice (rock, paper or scissors):")

while play:
    if player not in options:
        print("Sorry, that's not a valid choice.")
        player = input("Enter your choice (rock, paper or scissors):")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissor":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissor" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")

    print("Player:", player)
    print("Computer:", computer)
    play_again = input("Do you want to play again? (y/n): ")
    if play_again == "y":
        play = True
    else:
        play = False

