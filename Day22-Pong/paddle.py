"""Paddle class definition."""
from turtle import Turtle


class Paddle(Turtle):
    """Paddle Class."""

    id = 0
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.create()
        # self.move()
    
    def create(self):
        self.penup()
        self.speed("fastest")
        self.shape("square")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.setposition(self.x, self.y)

    def move_up(self):
        y_cor = self.ycor()
        if y_cor < 230:
            self.goto(x=self.x, y=y_cor + 30)

    def move_down(self):
        y_cor = self.ycor()
        if y_cor > -230:
            self.goto(x=self.x, y=y_cor - 30)
