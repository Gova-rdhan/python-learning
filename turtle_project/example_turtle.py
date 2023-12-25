import turtle
from turtle import Turtle,Screen
import turtle as tur
from turtle import Turtle,Screen
import random
t = Turtle()
tim = tur.Turtle()
sc = Screen()
turtle.colormode(255)
def random_colr():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tup = (r, g, b)
    return tup
tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(100)
tim.setheading(0)
no_of_dots = 101

for i in range(1,101):
    tim.dot(20,random_colr())
    tim.forward(50)
    if i % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
sc.exitonclick()