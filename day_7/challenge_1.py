#!/usr/bin/python3
# Day 7 _challenge 1_ for 100 days of code _ Range, Listss, IF/ELSE, Module,
# Strings, While loops.

"""
    The main focus for the day was developing the hangman project.
    The key concepts applied where flowchart programming.
"""
import random

# TODO-1
"""
    Randomly choose a word from the word_list and assign it to a variable
    called chosen_word.
"""
word_list = ['ardvark', 'baboon', 'camel']
chosen_word = random.choice(word_list)
blanks = len(chosen_word)

# TODO-2
"""
    Ask the user to guess a letter and assign their answer to a variable
    called guess. Make guess lowercase.
"""
guess = input("guess a letter in the word: ").lower()

# TODO-3
"""
    Check if the letter the user guessed (guess) is one of the letters in
    the chosen_word
"""
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
