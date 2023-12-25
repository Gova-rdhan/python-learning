import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
score = Scoreboard()
player = Player()
car = CarManager()
screen.listen()
screen.onkey(player.move_up,"Up")
screen.setup(width=600, height=600)
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car.car_create()
    car.move()
    for ca in car.cars:
        if ca.distance(player) < 20:
            game_is_on = False
            score.game_over()



    if player.ycor() > 280:
        score.levelup()
        player.reset_player()
        car.increase_speed()
        time.sleep(2)

    screen.update()
screen.exitonclick()
