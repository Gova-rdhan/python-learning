from turtle import Turtle,Screen
class Turtles:
    def __init__(self,color,position,position1,position2,direction,direction1,direction2):
        self.color = color
        self.position = position
        self.position1 = position1
        self.position2 = position2
        self.direction = direction
        self.direction1 = direction1
        self.direction2 = direction2

    def moving(self,obj):
        obj.forward(self.direction)
        obj.setheading(self.position1)
        obj.setheading(self.position)
        obj.forward(self.direction)
        obj.setheading(self.position)
        obj.forward(self.direction)