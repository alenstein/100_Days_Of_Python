from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

L_START_POSITION = (-350, 0)
R_START_POSITION = (350, 0)

screen = Screen()
ball = Ball()
score_lr = Scoreboard()
l_pad = Paddle(L_START_POSITION)
r_pad = Paddle(R_START_POSITION)
screen.listen()
screen.tracer(0)
game_is_on = True

screen.bgcolor('Black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.onkey(r_pad.go_up, 'Up')
screen.onkey(l_pad.go_up, 'w')
screen.onkey(r_pad.go_down, 'Down')
screen.onkey(l_pad.go_down, 's')

while game_is_on:
    screen.update()
    time.sleep(0.07)
    r_pad.color('white')
    l_pad.color('white')
    ball.move()

    # detect collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if ball.xcor() > 320 and ball.distance(r_pad) < 50 or ball.xcor() < -320 and ball.distance(l_pad) < 50:
        ball.bounce_x()
        if ball.distance(r_pad) < 50:
            r_pad.color('green')
        else:
            l_pad.color('green')

    # detect r_pad mis-collision
    if ball.xcor() > 380:
        r_pad.color('red')
        ball.reset_position("right")
        score_lr.l_scored()

    # detect l_pad mis-collision
    if ball.xcor() < -380:
        l_pad.color('red')
        ball.reset_position("left")
        score_lr.r_scored()

screen.exitonclick()
