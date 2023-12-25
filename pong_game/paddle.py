from turtle import Turtle
POSITION = [-310,310]
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.paddle = []
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)

    def move_up(self):
        new_cor = self.ycor() + 40
        self.goto(self.xcor(),new_cor)
    def move_down(self):
        new_cor = self.ycor() - 40
        self.goto(self.xcor(), new_cor)
    def position_setup(self,xcor,ycor):
        self.goto(xcor,ycor)