import random
import turtle
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your bet", prompt="Which turtle win the race?")
colors = ["red","orange","yellow","green","blue"]
all_turtle = []

y=-100
for _ in range(5):
    tim = Turtle(shape="turtle" )
    tim.color(colors[_])
    tim.penup()
    tim.goto(-240, y)
    y+=50
    all_turtle.append(tim)

if user_bet:
    is_race_on = True
while is_race_on:
    for tu in all_turtle:
        if tu.xcor() > 230:
            is_race_on=False
            if user_bet ==  tu.pencolor():
                print("You win")
            else:
                print("You lose")

        ran_distance = random.randint(0, 10)
        tu.forward(ran_distance)


screen.exitonclick()