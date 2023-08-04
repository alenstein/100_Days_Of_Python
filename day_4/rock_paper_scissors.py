"""
    Day  4 daily project.
    Rock, paper, scissors game with a computer
"""
import random

rock = "🤜"
paper = "🖐️"
scissors = "✀"

hand_signals = [rock, paper, scissors]
prompt = "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
player_signal = int(input(prompt))
computer_signal = random.randint(0, 2)

print(f"You chose: {hand_signals[player_signal]}")

print("Computer chose:", end = " ")
print(hand_signals[computer_signal])

# calculate who wins
if player_signal == computer_signal:
    print("It's a DRAW!\n")
elif player_signal == 0:
    if computer_signal == 1:
        print("You lose\n")
    else:
        print("You win!\n")
elif player_signal == 1:
    if computer_signal == 2:
        print("You lose\n")
    else:
        print("You win\n")
else:
    if computer_signal == 0:
        print("You lose\n")
    else:
        print("You win!\n")

