#!/usr/bin/python3
from turtle import Turtle, Screen

game_is_on = True


def setup():
    """
        Function initialised game enviroment,
        creates screen with required properties.

        Returns:
            screen (Screen): an object of Screen class
             in turtle module

    """
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('Black')
    screen.title('  Snake Game ')
    screen.tracer(0)
    screen.listen()

    return screen
