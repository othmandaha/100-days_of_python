from turtle import Turtle, Screen
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

def make_turtles():
    y = -100
    turtles = []
    for index, value in enumerate(colors, start=0):
        turtles.append(Turtle(shape='turtle'))
        turtles[index].color(value)
        turtles[index].penup()
        turtles[index].goto(x= -230, y=y)
        y += 33
    
    return turtles


screen = Screen()
screen.setup(width=500, height=400)


turtles = make_turtles()
race_on = False
answer = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter your bet: ")
if answer:
    race_on = True

while race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            race_on = False
        turtle.forward(random.randint(0, 10))

if winner == answer:
    print("You've won the winner color is {}".format(winner))
else:
    print("you've lost, the winning color is {}".format(winner))



screen.exitonclick()