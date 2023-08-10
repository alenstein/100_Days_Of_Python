#!/usr/bin/python3
# Day 7 _challenge 3_ for 100 days of code _ Range, Lists, IF/ELSE, Module,
# Strings, While loops.

"""
    The main focus for the day was developing the hangman project.
    The key concepts applied where flowchart programming.
    Challenge 3.
"""
import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

def load_display(display=[]):
    for letter in display:
        print(letter, end=" ")
    print()


# Create blanks
display = []
for _ in range(word_length):
    display += "_"

# TODO-1 
while '_' in display:
    guess = input("Guess a letter: ").lower()

    # loop through each position in the chosen word: 
    for index in range(len(chosen_word)):
        if chosen_word[index] == guess:
            display[index] = guess
        else:
            pass
    load_display(display)
    

print("you won!")
 
