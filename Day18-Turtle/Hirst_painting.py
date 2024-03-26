import turtle as t
import random

list_rgb = [(237, 251, 245), (249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20),
            (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49),
            (240, 245, 251), (244, 39, 149), (65, 202, 229), (14, 205, 222), (63, 21, 10),
            (224, 19, 111), (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9), (248, 11, 9),
            (222, 140, 203), (68, 240, 161), (10, 97, 62), (5, 38, 33), (68, 219, 155)]

#* -300 is when the loop should start
#* 200 is when the loop must stop

t.colormode(255)
tim = t.Turtle()

h = -250
v = -250

tim.penup()
tim.hideturtle()
while v < 250:
    h = -250
    while h < 250:
        tim.goto(h, v) #(horizontal, vertical)
        tim.dot(20, random.choice(list_rgb))

        h += 50
    v += 50

screen = t.Screen()
screen.exitonclick()
