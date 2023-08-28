from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, start_pos):
        super().__init__(shape='square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.penup()
        self.goto(start_pos)

    def go_up(self):
        ny = self.ycor() + 20
        self.goto(self.xcor(), ny)

    def go_down(self):
        ny = self.ycor() - 20
        self.goto(self.xcor(), ny)
