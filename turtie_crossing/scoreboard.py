FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.color("black")
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(-150,250)
        self.write(f"LEVEL {self.level}",align = 'right',font = FONT )
    def levelup(self):
        self.level += 1
        self.update_level()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER !!!!",align="center",font=FONT)
