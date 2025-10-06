import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars_speed = 0.1
        self.created_cars = []
        self.hideturtle()


    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle(shape="square")
            new_car.penup()
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            y_cor = random.randint(-239,240)
            new_car.goto(300,y_cor)
            self.created_cars.append(new_car)


    def move_cars(self):
        for car in self.created_cars:
            car.back(MOVE_INCREMENT)


    def turtle_collision_with_car(self,player):
        for car in self.created_cars:
            if car.distance(player) < 20:
                return True

