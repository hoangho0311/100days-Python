from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.penup()
        self.hideturtle()
        self.goto(-280, 280)
        self.update()

    def update(self):
        self.clear()
        self.write(f"level: {self.level}", align="left")

    def increaseScore(self):
        self.level+=1
        self.update()

    def gameOver(self):
        self.goto(0, 0)
        self.write("Game Over", align="left")