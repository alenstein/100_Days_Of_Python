#!/usr/bin/python3
# part 1 for snake game project

from turtle import Turtle, Screen
from gamedata import *
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = setup()
snake = Snake()

screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()
