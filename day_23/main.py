#!/usr/bin/python3

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
score = Scoreboard()
manager = CarManager()

screen.onkey(player.go_up, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    manager.create_cars()
    manager.go()

    # detect collision with car
    for car in manager.all_cars:
        if car.distance(player) < 30:
            game_is_on = False
            score.game_over()

    # detect when player reaches the other side
    if player.has_crossed():
        score.level += 1
        player.reset_game()
        manager.increase_speed()
        score.update_board()

screen.exitonclick()
