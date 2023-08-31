#!/usr/bin/python3

from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__(shape='turtle')
        self.penup()
        self.reset_game()
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def has_crossed(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def reset_game(self):
        self.goto(STARTING_POSITION)

