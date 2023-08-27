#!/usr/bin/python3
from turtle import Turtle, Screen
import random
from game_data import *

screen = Screen()
race_is_on = False
user_bet = ""

for t_index in range(6):
    racer = Turtle(shape="turtle")
    racer.color(colors[t_index])
    racer.penup()
    racer.goto(zero_states[t_index]['x'], zero_states[t_index]['y'])
    players.append(racer)


def move_forwards():
    racer.forward(30)


def clockwise():
    racer.right(10)


def counter_clockwise():
    racer.left(10)


def move_backwards():
    racer.backward(30)


def clean():
    racer.clear()
    racer.penup()
    racer.home()
    racer.pendown()


def setup():
    global user_bet

    screen.setup(width=800, height=800)
    user_bet: str = screen.textinput("Make your bet!", "Which turtle will win the race? Enter a color: ")
    shuffle_players()
    if user_bet is not None:
        return True


def shuffle_players():
    prev = 0
    while len(shuffled_players) < 6:
        rand_player = random.randint(0, 5)
        if rand_player == prev:
            pass
        else:
            if players[rand_player] in shuffled_players:
                pass
            else:
                shuffled_players.append(players[rand_player])
                prev = rand_player


def load_game():
    global race_is_on
    while race_is_on:
        displacement = random.randint(25, 36)
        for turtle in shuffled_players:
            if turtle.xcor() > 355:
                race_is_on = False
                winner = turtle.pencolor()
                return winner
            turtle.forward(displacement)


race_is_on = setup()
winning_color = load_game()

if user_bet == winning_color:
    print(f"Congratulations The color that won is actually {winning_color}!")
else:
    print(f"You lost, the color {winning_color} won!")
screen.exitonclick()
