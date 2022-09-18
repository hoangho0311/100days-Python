import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

paddle = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(paddle.up, "w")
screen.onkey(paddle.down, "s")
screen.onkey(paddle2.up, "Up")
screen.onkey(paddle2.down, "Down")

gameOn = True
while gameOn:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor()  < -280:
        ball.bounce()

    if ball.distance(paddle) < 50 and ball.xcor() > 340 or ball.distance(paddle2) < 50 and ball.xcor() < -340:
        ball.bun()

    if ball.xcor() > 390 :
        ball.refresh()
        score.increaseRscore()

    if ball.xcor()<-390:
        ball.refresh()
        score.increaseLscore()


screen.exitonclick()