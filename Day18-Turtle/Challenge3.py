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


tim.width(3)
for x in range(8):
    tim.pencolor(random.choice(tk_colors))
    i = 3 + x
    j = 360 / i
    while i > 0:
        tim.forward(100)
        tim.right(j)
        i -= 1




screen = Screen()
screen.exitonclick()