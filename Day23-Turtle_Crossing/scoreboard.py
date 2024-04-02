FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('black')
        self.level = 0 
        self.goto(x=-220, y=250)
        self.write("Level: 0", align="center", font=FONT)
        
    

    def update(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def gameover(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
