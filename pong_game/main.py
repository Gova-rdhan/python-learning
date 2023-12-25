from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

r_pad = Paddle()
l_pad = Paddle()
balll = Ball()
sc = Screen()
tur = Turtle()
player1 = Score()
player2 = Score()

r_pad.position_setup(-320,0)
l_pad.position_setup(312,0)
sc.tracer(0)
sc.screensize(600,600)
sc.bgcolor("black")
sc.title("Welcome to the Pong let's play.........")
sc.listen()
sc.onkey(r_pad.move_up,"w")
sc.onkey(r_pad.move_down,"s")
sc.onkey(l_pad.move_up,"Up")
sc.onkey(l_pad.move_down,"Down")

is_game_on = True
while is_game_on:
    sc.update()
    time.sleep(balll.move_spped)
    balll.move()
    if balll.ycor() == 270 or balll.ycor() == -270:
        balll.move_y()
    if balll.xcor() > 280 and balll.distance(l_pad) < 50:
        balll.move_x()
    if balll.distance(r_pad) < 50 and balll.xcor() == -300:
        balll.move_x()
    if balll.xcor() > 330:
        player1.r_point()
        balll.reset_position()
    if balll.xcor() < -330:
        player2.l_point()
        balll.reset_position()

sc.exitonclick()