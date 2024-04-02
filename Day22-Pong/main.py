from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

#* Setting the screen.
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)
screen.listen()

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = ScoreBoard()
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(left_paddle.move_up, 'w')
screen.onkeypress(left_paddle.move_down, 's')

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #* Collision with uper and buttom wall
    if  ball.ycor() >= 280 or ball.ycor() <= -280:
            ball.bounce_y()
    
    #* Collision with paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 330\
    or ball.distance(left_paddle) < 50 and ball.xcor() < -330:
          ball.bounce_x()
    
    #* Ball out of bound
    # left ball score
    if ball.xcor() > 420:
          time.sleep(0.4)
          scoreboard.l_point()
          ball.reset_position()
    #right ball score 
    if ball.xcor() < -420:
          time.sleep(0.4)
          scoreboard.r_point()
          ball.reset_position()
    
    


screen.exitonclick()