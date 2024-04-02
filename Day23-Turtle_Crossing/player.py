from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 14


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.color('Black')
        self.setheading(90)
        self.goto(STARTING_POSITION)
    
    def move(self):
        y_cor =self.ycor()
        self.goto(x=0, y=y_cor + MOVE_DISTANCE)
    
    def reset_position(self):
        self.goto(STARTING_POSITION)
    
    

