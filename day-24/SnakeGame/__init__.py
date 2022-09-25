import time
from turtle import Screen
from Snake import Snake
from food import Food
from score import score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = score()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.back, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.left, "a")

gameOn = True
while gameOn:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Collision
    if snake.head.distance(food) < 15:
        food.refesh()
        snake.extend()
        score.increase_score()

    if snake.head.xcor() >280 or snake.head.ycor() >280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()
screen.exitonclick()
