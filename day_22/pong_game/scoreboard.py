#!/usr/bin/python3

from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Georgia', 20, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = -1
        self.goto(0, 270)
        self.latest_score = f"Score: {self.score + 1}"
        self.color("Blue")
        self.update_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.latest_score = f"Score: {self.score}"
        self.write(self.latest_score, False, ALIGNMENT, FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, ALIGNMENT, FONT)