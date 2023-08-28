#!/usr/bin/python3
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.color('white')
        self.penup()
        self.goto(0, 0)
        self.y_move = 10
        self.x_move = 10

    def move(self):
        nx = self.xcor() + self.x_move
        ny = self.ycor() + self.y_move
        self.goto(nx, ny)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

