#!/usr/bin/python3
# Day 7 _challenge 4_ for 100 days of code _ Range, Lists, IF/ELSE, Module,
# Strings, While loops.

"""
    The main focus for the day was developing the hangman project.
    The key concepts applied where flowchart programming.
    Challenge 4.
"""
import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False

def load_display(display=[]):
    for letter in display:
        print(letter, end=" ")
    print()

stages = ['''
          +---+
          |   |
          0   |
         /|\  |
         / \  |
              |
        ========= 
        ''', '''
          +---+
          |   |
          0   |
         /|\  |
         /    |
              |
        ========= 
        ''', '''
          +---+
          |   |
          0   |
         /|\  |
              |
              |
        =========
        ''', '''
          +---+
          |   |
          0   |
         /|   |
              |
              |
        =========           
        ''', '''
          +---+
          |   |
          0   |
         /    |
              |
              |
        =========
        ''', '''
          +---+
          |   |
          0   |
              |
              |
              |
        =========
        ''', '''
          +---+
          |   |
              |
              |
              |
              |
        =========
        ''']

lives = 6
# Create blanks
display = []
for _ in range(word_length):
    display += "_"

# TODO-1 
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # loop through each position in the chosen word: 
    for index in range(len(chosen_word)):
        if chosen_word[index] == guess:
            display[index] = guess
    lives -= 1
    print(stages[lives])
    if lives == 0:
        end_of_game = True
        print("You lose!")
    load_display(display)
    if '_' not in display:
        end_of_game = True
        print("You win!")



