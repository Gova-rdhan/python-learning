from turtle import Turtle , Screen
sc = Screen()
speed = 20
pos = [0, -20, -40]
up = 90
down = 270
left = 180
right = 0
tu = Turtle()
class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.is_start = True
        self.head = self.snake[0]
    def create_snake(self):
        for seg in pos:
            self.add_snake(seg,0)
    def add_snake(self,position,y_cor):
        tur = Turtle(shape="square")
        tur.color("white")
        tur.penup()
        tur.goto(position,y_cor)
        self.snake.append(tur)
    def reset_snake(self):
        for sna in self.snake:
            sna.goto(1000,100)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]
    def extend(self):
        self.add_snake(self.snake[-1].xcor(),self.snake[-1].ycor())
    def move(self):
        for seg in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg - 1].xcor()
            new_y = self.snake[seg - 1].ycor()
            self.snake[seg].goto(new_x, new_y)
        self.head.forward(speed)

    def go_up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def go_down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def left_side(self):
        if self.head.heading() != right:
           self.head.setheading(left)

    def right_side(self):
        if self.head.heading() != left:
           self.head.setheading(right)

