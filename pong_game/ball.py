from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(10)
        self.color("white")
        self.shape("circle")
        self.shapesize(1,1)
        self.goto(0,0)
        self.xmove = 10
        self.ymove = 10
        self.lscore= 0
        self.rscore = 0
        self.move_spped = 0.1


    def move(self):
        x_cor = self.xcor() + self.xmove
        y_cor = self.ycor() + self.ymove
        self.goto(x_cor, y_cor)
    def move_y(self):
        self.ymove *= -1

    def move_x(self):
        self.xmove *= -1
        self.move_spped *= 0.9
    def reset_position(self):
        self.goto(0,0)
        self.move_spped = 0.1
        self.move_x()

