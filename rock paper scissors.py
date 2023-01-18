import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

player_move = input("Choose [r]rock, [p]paper or [s]scissors: ")

if player_move == "r":
    player_move = rock
elif player_move == "p":
    player_move = paper
elif player_move == "s":
    player_move = scissors
else:
    raise SystemExit("Invalid Input. Try again...")

computer_possible_action = ["r", "p", "s"]
computer_action = random.choice(computer_possible_action)
computer_move = ""

if computer_action == "r":
    computer_move = rock
elif computer_action == "p":
    computer_move = paper
else:
    computer_move = scissors

print(f"The computer chose {computer_move}")

if (player_move == rock and computer_move == scissors) or (player_move == paper and computer_move == rock) or (player_move == scissors and computer_move == paper):
    print("You win!")
elif player_move == computer_move:
    print("Draw!")
else:
    print("You lose!")