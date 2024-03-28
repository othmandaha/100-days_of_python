"""Snake class definition"""
from turtle import Turtle

MOVE_DISTANCE = 20
class Snake():

    def __init__(self):
        self.segs = []
        self.make()
        self.head = self.segs[0]
    def make(self):
        """Returns a list of 3 horizontally aligned squares"""
        x = 0
        for i in range(0, 3):
            self.segs.append(Turtle("square"))
            self.segs[i].penup()
            self.segs[i].color("white")
            self.segs[i].setx(x)
            self.segs[i].speed(1)
            x -= 20
    
    def extend(self):
        position = self.segs[-1].position()
        new_seg = Turtle("square")
        new_seg.penup()
        new_seg.color("white")
        new_seg.speed(1)
        new_seg.goto(position)
        self.segs.append(new_seg)

    def move(self):
        for i in range(len(self.segs) - 1, 0, -1):
            x = self.segs[i - 1].xcor() 
            y = self.segs[i - 1].ycor()
            self.segs[i].goto(x, y)
        self.segs[0].forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)