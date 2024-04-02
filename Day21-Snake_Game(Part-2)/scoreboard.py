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
        with open("Day21-Snake_Game(Part-2)\highscore.txt", 'r') as file:
            self.high_score = int(file.read())
        self.write(f"score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 20, "normal"))
    
    def update_s(self):
        self.clear()
        self.score += 1 
        self.write(f"score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 20, "normal"))

    def reset(self):
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Day21-Snake_Game(Part-2)\highscore.txt", 'w') as file:
                file.write(str(self.high_score)) 
        self.score = 0
        self.write(f"score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 20, "normal"))
    
    # def gameover(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER!", align="center", font=("Arial", 20, "normal"))

    
