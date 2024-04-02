import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.move, 'Up')
cars = []

game_is_on = True
i = 0
while game_is_on:

    #*Generate a car every 6th time the loops runs
    if i == 0:
        cars.append(CarManager())
        i = 6
    i -= 1

    #*Move and detect colission 
    cars_copy = cars.copy()
    for car in cars_copy:
        car.move()

        #* remove the cars that are out of screen
        if car.xcor() < -350:
            cars.remove(car)

        #*detect collission 
        if player.distance(car) < 20:
            scoreboard.gameover()
            game_is_on = False


    #* Finish line
    if player.ycor() > 280:
    #* Update score
        scoreboard.update()
    #*increase speed
        CarManager.increasespeed()
    #* Reset position
        player.reset_position()
        



    #*Update screen
    time.sleep(0.1)
    screen.update()


screen.exitonclick()