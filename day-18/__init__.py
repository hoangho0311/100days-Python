import random
from turtle import Turtle, Screen
color = ["yellow", "red" , "blue", "black", "pink"]
directions = [0, 90, 180, 270]
timmy_turtle = Turtle()
# timmy_turtle.pensize(10)
# for _ in range(3):
#     timmy_turtle.forward(10)
#     timmy_turtle.penup()
#     timmy_turtle.forward(10)
#     timmy_turtle.pendown()

# for i in range(3,10):
#     goc = 360 / i
#     for n in range(i):
#             timmy_turtle.color(random.choice(color))
#             timmy_turtle.right(goc)
#             timmy_turtle.forward(40)


# for _ in range(20):
#         timmy_turtle.color(random.choice(color))
#         timmy_turtle.forward(30)
#         timmy_turtle.setheading(random.choice(directions))

timmy_turtle.dot(20, "red")
screen = Screen()
screen.exitonclick()