#!/usr/bin/python3
from turtle import Turtle, Screen

t0 = Turtle()
screen = Screen()


def mv_forw():
    t0.forward(72)


def trig():
    t0.right(90)


def tlef():
    t0.left(270)


screen.listen()
screen.onkey(mv_forw, "f")
screen.onkey(trig, 'r')
screen.onkey(tlef, 'l')
screen.exitonclick()
