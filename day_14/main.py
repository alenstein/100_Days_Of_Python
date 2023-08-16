#!/usr/bin/python3
# Final project for day 14 - Higher or Lower

import random
import art
import game_data

end_of_game = False
score = 0

def pick_people():
    person_A = random.randint(1, len(game_data.data) - 1)
    person_B = random.randint(1, len(game_data.data) - 1)
    
    if person_A == person_B:
        pick_people()
    else:
        return [game_data.data[person_A], game_data.data[person_B]]


def print_data(person={}, index=''):
    name = person['name']
    descr = person['description']
    country = person['country']

    print(f'Compare {index}: {name}, a {descr}, from {country}.')
    return person['follower_count']


def eval(ans='', followers_A=0, followers_B=0):
    global score
    if ans not in ['A', 'B']:
        print("ERROR: invalid input!\n Game Over")
               
    if followers_A > followers_B:
        if ans == 'A':
            score += 1 
        elif ans == 'B':
            print(f"You Lose. score: {score}")
            end_of_game = True
            score = 0
    elif followers_B > followers_A:
        if ans == 'B':
            score += 1 
        elif ans == 'A':
            print(f"You Lose. score: {score}")
            end_of_game = True
            score = 0
    else:
        print('You lose score: {score}')
        end_of_game = True
        score = 0
    return score

while not end_of_game:
    print(art.logo)
    if score > 0:
        print('\033c', end="")
        print(art.logo)
        print(f"You're right! Current score: {score}.")
    people = pick_people()
    count_A = print_data(people[0], 'A')
    print(art.vs)
    count_B = print_data(people[1], 'B')
    
    answer = input("Who has more followers? Type 'A' or 'B': ").upper()
    score = eval(answer, count_A, count_B)
    if score == 0:
        print("\n================================================================\n")

