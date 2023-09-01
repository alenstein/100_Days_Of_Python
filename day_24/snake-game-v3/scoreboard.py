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
        with open("data.txt", 'r') as dat:
            self.high_score = int(dat.read())
        self.goto(0, 270)
        self.latest_score = f"Score: {self.score + 1}"
        self.color("Blue")
        self.update_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.latest_score = f"Score: {self.score} High Score: {self.high_score}"
        self.write(self.latest_score, False, ALIGNMENT, FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as dat:
                dat.write(f"{self.high_score}")
        self.score = 0
        self.update_score()
