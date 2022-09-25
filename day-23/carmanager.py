import random
from turtle import Turtle

class CarManager:
    def __init__(self):
        self.all_cars=[]
        self.carSpeed = 5

    def create_cars(self):
        randomChance = random.randint(1,6)
        if randomChance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color("black")
            new_car.goto(300, random.randint(-250,250))
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.carSpeed)

    def levelUp(self):
        self.carSpeed += 10