from turtle import Turtle,Screen,TurtleScreen

tur = Turtle()
screen = Screen()

def forward():
    tur.forward(10)
def backward():
    tur.setheading(tur.forward(tur.heading()-10))
def clockwise():
    tur.setheading(tur.heading()+10)
def anticlockwise():
    tur.forward(10)

def clear():
    tur.clear()
    tur.penup()
    tur.home()
    tur.pendown()

screen.listen()
screen.onkey(forward,"f")
screen.onkey(backward,"b")
screen.onkey(clockwise,"c")
screen.onkey(anticlockwise,"a")
screen.onkey(clear,"r")
screen.exitonclick()