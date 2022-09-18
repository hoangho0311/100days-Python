from turtle import Turtle
starting_postitions = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20

class Snake:

    def __init__(self):
        self.segments = []
        self.createSnake()
        self.head = self.segments[0]

    def createSnake(self):
        for position in starting_postitions:
            self.add_segment(position)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            newx = self.segments[i - 1].xcor()
            newy = self.segments[i - 1].ycor()
            self.segments[i].goto(newx, newy)
        self.segments[0].forward(move_distance)

    def add_segment(self, position):
        self.segment = Turtle("square")
        self.segment.color("white")
        self.segment.penup()
        self.segment.goto(position)
        self.segments.append(self.segment)

    def extend(self):
        print(self.segments[-1].position())
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def back(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)