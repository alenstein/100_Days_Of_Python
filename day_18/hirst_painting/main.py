#!/usr/bin/python3
# Day 18 final project - Replicating the hirst painting
import random
import turtle

# import colorgram
from turtle import Turtle, Screen

rgb_colors = []
for num in range(180):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    new_color = (r, g, b)
    rgb_colors.append(new_color)
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     rgb_colors.append(color.rgb)

tx = Turtle()
turtle.colormode(255)
tx.speed("fastest")

tx.penup()
tx.setheading(225)
tx.forward(300)
tx.setheading(0)
tx.pendown()

for dot in range(1, 360):
    tx.dot(36, random.choice(rgb_colors))
    tx.penup()
    tx.forward(60)
    if dot % 10 == 0:
        tx.setheading(90)
        tx.forward(60)
        tx.setheading(180)
        tx.forward(600)
        tx.setheading(0)
    tx.pendown()

screen = Screen()
Screen().exitonclick()
