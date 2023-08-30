#!/usr/bin/python3
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.color('white')
        self.penup()
        self.goto(0, 0)
        self.y_move = 6
        self.x_move = 6
        self.move_speed = 0.08

    def move(self):
        nx = self.xcor() + self.x_move
        ny = self.ycor() + self.y_move
        self.goto(nx, ny)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self, rev):
        self.goto(0, 0)
        if rev == 'left':
            self.x_move *= 1
        elif rev == 'right':
            self.x_move *= 1
        self.move_speed = 0.08
