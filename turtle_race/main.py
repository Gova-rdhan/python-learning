import random
from turtle import Turtle,Screen
colors = ["red","blue","green","yellow","orange","purple"]
sc = Screen()
sc.setup(width=500,height=400)
user_input = sc.textinput("make your bet","guess which color is the winner")
y_pos = [-150,-100,-50,0,50,100]
ob = []
for index in range(0,6):
    tur1 = Turtle(shape='turtle')
    tur1.penup()
    tur1.goto(x=-230, y=y_pos[index])
    tur1.color(colors[index])
    ob.append(tur1)
is_race_on = False
if user_input:
    is_race_on = True
while is_race_on:
    for turtle in ob:
        if turtle.xcor() > 200:
            winner = turtle.pencolor()
            is_race_on = False
            if winner == user_input:
                print(f"yes youre correct!!!!! The winner is {winner}")
            else:
                print(f"oops youre wrong!!!!! The winner is {winner}")
        speed = random.randint(1,10)
        turtle.forward(speed)

sc.exitonclick()