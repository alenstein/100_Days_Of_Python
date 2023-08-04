# Day 4 for 100 days of code _ Randomisation and Lists

# exercise_1 - generating different types of numbers.
import random

random_integer = random.randint(1, 10)
print(f'random number generated: {random_integer}')

random_float = random.uniform(1, 23)
print(f'random float generated: {random_float}\n')

# exercise_2 - who's paying?
""" 
    Program which will select a random name from a list of names.
    The person selected will have to pay for everybody's food bill.
"""
names_string = input("Enter the names of all people participating.\n(make sure to separate them using a comma then space.): \n")

names = names_string.split(', ')

random_index = random.randint(0, len(names))
payee = names[random_index]
print(f'{payee} is going to buy the meal today!\n')

# exercise_3 - Treasure Map
""" Program which will mark a spot with an X. """
treasure_map = [['⏹️', '⏹️', '⏹️'], ['⏹️', '⏹️', '⏹️'], ['⏹️', '⏹️', '⏹️']]
print(treasure_map[0])
print(treasure_map[1])
print(treasure_map[2])
position = input("which position do you want to put the treasure:  ")
pos_x = int(position[0]) - 1
pos_y = int(position[1]) - 1
treasure_map[pos_x][pos_y] = 'X'

print(treasure_map[0])
print(treasure_map[1])
print(treasure_map[2])
