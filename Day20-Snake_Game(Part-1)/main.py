from turtle import Screen, Turtle
import time
from snake import Snake

#* Screen Configuration
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Le3ba dyal l7nech')
screen.tracer(0)


#* Make The initial Snake





game_on = True
snake = Snake()
screen.listen()
screen.update()
while game_on:
    screen.update()
    time.sleep(0.09)
    snake.move()
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")

screen.exitonclick()
