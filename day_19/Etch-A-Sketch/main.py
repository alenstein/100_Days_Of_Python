#!/usr/bin/python3
from turtle import Turtle, Screen

drawer = Turtle()
screen = Screen()


def move_forwards():
    drawer.forward(30)


def clockwise():
    drawer.right(10)


def counter_clockwise():
    drawer.left(10)


def move_backwards():
    drawer.backward(30)


def clean():
    drawer.clear()
    drawer.penup()
    drawer.home()
    drawer.pendown()


screen.listen()
screen.onkey(move_forwards, "W")
screen.onkey(clockwise, 'D')
screen.onkey(counter_clockwise, 'A')
screen.onkey(move_backwards, 'S')
screen.onkey(clean, 'C')
screen.exitonclick()
