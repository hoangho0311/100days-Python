from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.xmove = 10
        self.ymove = 10

    def move(self):
        self.goto(self.xcor()+self.xmove, self.ycor()+self.ymove)

    def bounce(self):
        self.ymove *= -1

    def bun(self):
        self.xmove*=-1

    def refresh(self):
        self.goto(0,0)
        self.bun()