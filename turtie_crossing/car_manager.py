COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 10
from turtle import Turtle
import random
class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE


    def car_create(self):
        chance = random.randint(1,6)
        if chance == 1:
            new_Car = Turtle()
            new_Car.penup()
            new_Car.shape("square")
            new_Car.shapesize(1,2,1)
            new_Car.color(random.choice(COLORS))
            y_cor = random.randint(-250,250)
            new_Car.goto(300,y_cor)
            self.cars.append(new_Car)
    def move(self):
        for i in self.cars:
            i.backward(STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        self.car_speed += 10
