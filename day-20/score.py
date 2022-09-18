from turtle import Turtle

class score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 250)

        self.write(f"Score: {self.score}", align="center", font=("courier", 20, "normal"))
        self.hideturtle()

    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("courier", 20, "normal"))

    def GameOver(self):
        self.goto(0,0)
        self.clear()
        self.write(f"Game Over", align="center", font=("courier", 30, "normal"))