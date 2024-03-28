from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

#* Screen Configuration
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Le3ba dyal l7nech')
screen.tracer(0)


#* Make The initial Snake
game_on = True
snake = Snake()
food = Food()
screen.listen()
screen.update()

#* Moving 
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
score = ScoreBoard()


while game_on:
    screen.update()
    time.sleep(0.09)
    snake.move()

    #* Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        score.update_s()
        snake.extend()

    #* Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < - 295\
    or snake.head.ycor() > 280 or snake.head.ycor() < - 295:
        game_on = False
        score.gameover()
    
    #* Detect collision with tail.
    for seg in snake.segs:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg) < 10:
            game_on = False
            score.gameover()





screen.exitonclick()