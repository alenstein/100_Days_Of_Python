"""
    Day 3 project - Treasure island.
    This is an adventure game with a mission for finding a treasure.
"""

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
step_1 = input("You're at a cross road. Where do you want to go? Type \"Left\" or \"right\" ")

if step_1 == "left":
    step_2 = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.")
    if step_2 == "wait":
        step_3 = input("You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?. ")
        if step_3 == "Yellow":
            print("You Win!")
        else:
            print("Game Over!")
    else:
        print("Attacked by trout.\n Game Over.")
else:
    print("You fell into a hole.\n Game Over.")
