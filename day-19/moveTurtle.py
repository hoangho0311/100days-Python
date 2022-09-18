from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move():
    tim.forward(10)
def back():
    tim.back(10)
def rotate():
    tim.left(10)
def clear():
    tim.clear()
screen.listen()
screen.onkey(key="w", fun=move)
screen.onkey(key="s", fun=back)
screen.onkey(key="a", fun=rotate)
screen.onkey(key="d", fun=rotate)
screen.onkey(key="c", fun=clear)


screen.exitonclick()