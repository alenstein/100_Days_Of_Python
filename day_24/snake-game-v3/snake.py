#!/usr/bin/python3
from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


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
        self.head.forward(MOVE_DISTANCE)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self, position):
        new_snake_segment = Turtle(shape="square")
        new_snake_segment.color("white")
        new_snake_segment.penup()
        new_snake_segment.goto(position)
        self.segments.append(new_snake_segment)

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

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

    def reset(self):
        for segment in self.segments:
            segment.goto(2000, 2000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

