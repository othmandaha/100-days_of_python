import turtle as t
import random


t.colormode(255)
tim = t.Turtle()
tim.speed(0)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


i = 0
while i <= 360:
    tim.color(random_color())
    tim.setheading(i)
    tim.circle(100)
    i += 5

screen = t.Screen()
screen.exitonclick()