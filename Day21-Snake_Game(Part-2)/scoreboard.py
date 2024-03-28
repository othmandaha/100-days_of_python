"""The scoreboard class definition."""
from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.sety(250)
        self.score = 0
        self.write(f"score: {self.score}", align="center", font=("Arial", 20, "normal"))
    
    def update_s(self):
        self.clear()
        self.score += 1 
        self.write(f"score: {self.score}", align="center", font=("Arial", 20, "normal"))
    
    def gameover(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=("Arial", 20, "normal"))

    
