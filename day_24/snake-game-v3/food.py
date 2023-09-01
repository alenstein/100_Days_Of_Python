#!/usr/bin/python3

from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')
        self.shift_position()

    def shift_position(self):
        ran_x = randint(-280, 280)
        ran_y = randint(-280, 265)
        self.goto(ran_x, ran_y)

