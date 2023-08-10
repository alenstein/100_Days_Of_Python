#!/usr/bin/python3
"""
    Module contains all the control logic and rendering of the game's CLI UI.
"""

import random
import hangman_words
import hangman_art

# update the word list to use the word_list from hangman_words.py
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# import the logo from the hangman_art.py and print it.
print(hangman_art.logo)

# code test
print(f'Pssst - the solution is {chosen_word}')

# create the blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # if the user has entered a letter they've already guessed,
    # the letter and let them know.
    if guess in display:
        print("letter: {guess} already entered. Try again!")

    # Check the guessed letter
    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter
    
    # Check if user is wrong.
    if guess not in chosen_word:
        # if the letter is not in the chosen_word, print out the letter and
        # let them know it's not in the word.
        print(f"letter: {guess} not in the chosen word.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("\n\t\t\t\tYou Lose.!!")
    # Join all the elements in the list and turn it into a String
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if '_' not in display:
        end_of_game = True
        print("You win.")

    # import the stages from hangman_art.py and render them accordingly
    print(hangman_art.stages[lives])
