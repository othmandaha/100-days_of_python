from turtle import Turtle, Screen
import random
tk_colors = [
    "Alice Blue", "Antique White", "Aqua", "Aquamarine", "Azure", "Beige", "Bisque", "Black", "Blanched Almond",
    "Blue", "Blue Violet", "Brown", "Burlywood", "Cadet Blue", "Chartreuse", "Chocolate", "Coral",
    "Cornflower Blue", "Cornsilk", "Crimson", "Cyan", "Dark Blue", "Dark Cyan", "Dark Goldenrod", "Dark Gray",
    "Dark Green", "Dark Khaki", "Dark Magenta", "Dark Olive Green", "Dark Orange", "Dark Orchid", "Dark Red",
    "Dark Salmon", "Dark Sea Green", "Dark Slate Blue", "Dark Slate Gray", "Dark Turquoise", "Dark Violet",
    "Deep Pink", "Deep Sky Blue"
]

tim = Turtle()
tim.speed(0)

directions = [tim.right, tim.left, tim.forward, tim.backward]
tim.width(15)

while True:
    tim.color(random.choice(tk_colors))
    rand = random.choice(directions)
    if rand == tim.forward or rand == tim.backward:
        rand(30)
    else:
        tim.forward(30)
        rand(90)

screen = Screen()
screen.exitonclick()