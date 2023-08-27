#!/usr/bin/python3
from turtle import Turtle


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            self.segments[seg].penup()
            nx = self.segments[seg - 1].xcor()
            ny = self.segments[seg - 1].ycor()
            self.segments[seg].goto(nx, ny)

        self.head.penup()
        self.head.forward(20)

    def create_snake(self):
        for t_index in range(3):
            new_snake_segment = Turtle(shape="square")
            new_snake_segment.color("white")
            new_snake_segment.penup()
            new_snake_segment.goto(t_index * -20, t_index)
            self.segments.append(new_snake_segment)
            new_snake_segment.pendown()

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
