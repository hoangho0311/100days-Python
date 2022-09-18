from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore = 0
        self.rscore = 0
        self.updateScore()

    def updateScore(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.lscore, align="center", font=("Aria", 30, "normal"))
        self.goto(100, 200)
        self.write(self.rscore, align="center", font=("Aria", 30, "normal"))

    def increaseLscore(self):
        self.lscore+=1
        self.updateScore()

    def increaseRscore(self):
        self.rscore+=1
        self.updateScore()
