from turtle import Turtle,Screen
import random
tur =Turtle()
tur1 =Turtle()
tur2 =Turtle()
tur3 =Turtle()
tur4 =Turtle()
sc = Screen()
def race(obj):
    obj.shape("turtle")
    obj.penup()
    if obj == 'tur':
        obj.color("red")
    elif obj == 'tur1':
        obj.color("blue")
        obj.setheading(270)
        obj.forward(25)
        obj.setheading(180)
    elif obj == 'tur2':
        obj.color("green")
        obj.setheading(270)
        obj.forward(50)
        obj.setheading(180)
    elif obj == 'tur3':
        obj.color("yellow")
        obj.setheading(270)
        obj.forward(75)
        obj.setheading(180)
    else:
        obj.color("pink")
        obj.setheading(270)
        obj.forward(100)
        obj.setheading(180)
    obj.setheading(180)
    obj.forward(300)
    obj.setheading(0)
    for _ in range(100):
        obj.forward(random.randint(1, 10))

race(tur)
race(tur1)
race(tur2)
race(tur3)
sc.exitonclick()