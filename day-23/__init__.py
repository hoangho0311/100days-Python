import time
from turtle import Screen
from player import Player
from carmanager import CarManager
from scoreboara import ScoreBoard

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

player = Player()
car = CarManager()
score = ScoreBoard()

screen.listen()
screen.onkey(player.go_up,"w")

gameOn = True
while gameOn:
    time.sleep(0.1)
    screen.update()

    car.create_cars()
    car.move_car()

    for cars in car.all_cars:
        if cars.distance(player) < 20:
            gameOn = False
            score.gameOver()

    if player.is_at_finish_line():
        player.go_to_start()
        score.increaseScore()
        car.levelUp()


screen.exitonclick()
