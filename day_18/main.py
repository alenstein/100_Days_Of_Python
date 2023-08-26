#!/usr/bin/python3
import turtle
from turtle import Turtle, Screen
import random

t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()
t5 = Turtle()
colors = ['red', 'green', 'blue', 'Orange', 'teal', 'cyan', 'black', 'violet']
dirs = [0, 90, 180, 270]
t1.shape("circle")
t1.color("red")
turtle.colormode(255)


def generate_color():
    """

    Returns:
        tuple with 3 values for Red Green and Blue
    """
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


# # challenge 1
# for _ in range(4):
#     t1.forward(300)
#     t1.right(90)
#
# # challenge 2
# for _ in range(15):
#     t2.forward(10)
#     t2.penup()
#     t2.forward(10)
#     t2.pendown()

# challenge 3

# for num_of_sides in range(3, 16):
#     t3.color(colors[(num_of_sides - 3) % len(colors)])
#     for _ in range(num_of_sides):
#         angle = 360 / num_of_sides
#         t3.forward(100)
#         t3.right(angle)


# # challenge 4
# t4.pensize(15)
# t4.speed("fastest")
# for _ in range(1200):
#     t4.color(generate_color())
#     t4.forward(45)
#     t4.setheading(random.choice(dirs))


# challenge 5
def draw_spiro(size):
    for _ in range(int(360 / size)):
        t5.speed("fastest")
        t5.color(generate_color())
        t5.circle(250)
        curr_heading = t5.heading()
        t5.setheading(curr_heading + 10)


draw_spiro(5)
screen = turtle.Screen()
Screen().exitonclick()

