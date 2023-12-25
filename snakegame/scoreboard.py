from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        with open("textfile") as data:
            self.highscore = int(data.read())
        self.updata_score()



    def updata_score(self):
        self.write(f"Score : {self.score} High Score {self.highscore}", align="center", font=("Arial", 10, "normal",))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.updata_score()

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("textfile",mode='w') as data:
                data.write(f"{self.highscore}")
        self.score = 0

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align="center", font=("Arial", 10, "normal",))