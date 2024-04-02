"""ball class definition"""
from turtle import Turtle


class Ball(Turtle):
    """The ball class."""

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.penup()
        self.y_move = 2
        self.x_move = 2 
        self.move_speed = 0.01
    
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y) 

    def bounce_y(self):
        """Redirects the y axis movement to the opposite direction."""
        self.y_move *= -1

    def bounce_x(self):
        """Refactors the x axis movement to the opposite direction."""
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """Resets the position to the center and changes the movement."""
        self.move_speed = 0.01
        self.goto(0, 0)
        self.bounce_x()
    