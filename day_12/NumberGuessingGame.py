#!/usr/bin/python3
# Number Guessing game project for day 12.

import art
import random

difficulty = {
    'easy': 10,
    'hard': 5,
}

end_of_game = False


def game_mode(attempts=''):
    return int(difficulty[attempts])


def rank_guess(num=0, guess=0):
    if num == guess:
        print(f"You got it! The answer is {num}.")
    elif guess  < num:
        print("Too low")
    elif guess > num:
        print("Too High")
    elif guess > 100 and guess < 1:
        print(f"Number out of range!")
    else:
        print("Invalid guess")


def reload_game():
    attempts = 0
    ans = input("Guess again? Type 'y' or 'n': ").lower()
    if ans == 'y':
        end_of_game = False
    elif ans == 'n':
        end_of_game = True 
    else:
        print("ERROR: Invalid input.")
        reload_game()


def initialise_game():
    """Function loads the game to its zero state. it basically resets the game."""
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
    number_of_attempts = game_mode(mode)
    print(f"You have {number_of_attempts} remaining to guess the number.")
    return number_of_attempts
    
    
while not end_of_game:
    print("\033c", end="")
    attempts = initialise_game()
    
    # get game data
    answer = random.randint(1, 100)
    guess = int(input("Make a guess: "))
   
    while attempts > 0:
        # compare guess with correct answer
        rank_guess(answer, guess)
        if not answer == guess:
            attempts -= 1
        
            if attempts <= 0:
                print("You've run out of guesses, you lose.")
                reload_game()
            else:
                print("Guess again")
                guess = int(input("Make a guess: "))        
                end_of_game = False
        else:
            attempts = 0
