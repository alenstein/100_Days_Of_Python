#!/usr/bin/python3

from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Georgia', 20, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.color("Blue")
        self.update_score()

    def update_score(self):
        self.goto(-100, 200)
        self.write(self.l_score, False, ALIGNMENT, FONT)
        self.goto(100, 200)
        self.write(self.r_score, False, ALIGNMENT, FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, ALIGNMENT, FONT)

    def l_scored(self):
        self.l_score += 1
        self.clear()
        self.update_score()

    def r_scored(self):
        self.r_score += 1
        self.clear()
        self.update_score()
