from turtle import Turtle

class score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.hScore = int(data.read())
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 250)
        self.write(f"Score: {self.score} High Score: {self.hScore}", align="center", font=("courier", 20, "normal"))


    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.hScore}", align="center", font=("courier", 20, "normal"))

    def reset(self):
        if self.score > self.hScore:
            self.hScore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.hScore}")
        self.score = 0
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.hScore}", align="center", font=("courier", 20, "normal"))