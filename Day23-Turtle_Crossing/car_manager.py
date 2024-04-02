from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    move_distance = STARTING_MOVE_DISTANCE
    

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.turtlesize(stretch_len=2, stretch_wid=1)
        self.goto(x= 320, y=random.randint(-200, 280))
        self.color(random.choice(COLORS))

    def move(self):
        x_axis = self.xcor() 
        y_axis = self.ycor()
        self.goto(x=x_axis - CarManager.move_distance, y=y_axis)

    @classmethod
    def increasespeed(self):
        CarManager.move_distance += MOVE_INCREMENT