import random
command = input("Въведете своя избор: ")
options = ("rock", "paper", "scissor")
computer_choice = random.choice(options)
print(f"Избора на компютъра е: {computer_choice}")

if command == computer_choice:
    print("EQUALS")
elif command == "rock" and computer_choice == "paper":
    print("Computer wins!")
elif command == "paper" and computer_choice == "scissor":
    print("Computer wins!")
elif command == "scissor" and computer_choice == "rock":
    print("Computer wins!")
else:
    print("You win")