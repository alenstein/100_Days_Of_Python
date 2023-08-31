#!/usr/bin/python3

from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = 'left'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.color('Black')
        self.goto(-280, 260)
        self.update_board()

    def update_board(self):
        new_level = f"Level: {self.level}"
        self.clear()
        self.write(new_level, False, ALIGNMENT, FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", FONT)

