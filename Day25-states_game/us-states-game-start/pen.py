from turtle import Turtle


class Pen(Turtle):
    """A class representing a pen for writing text on the screen."""

    def __init__(self, answer, x, y):
        """
        Initialize a Pen object.

        Args:
            answer (str): The text to write on the screen.
            x (int): The x-coordinate for the pen's starting position.
            y (int): The y-coordinate for the pen's starting position.
        """
        super().__init__()
        self.penup()
        self.color('black')
        self.speed('fastest')
        self.goto(x=x, y=y)
        self.hideturtle()
        self.write(answer, align="center", font=("Arial", 13, "normal"))
