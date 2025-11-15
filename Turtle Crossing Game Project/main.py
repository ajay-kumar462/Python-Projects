import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

tim = Player()

screen.listen()
screen.onkey(tim.move_forward, "Up")

level = Scoreboard()

car_list = []
for i in range(20):
    i = CarManager()
    car_list.append(i)
    i.penup()
    i.goto(random.randint(-250, 250), random.randint(-250, 250))


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if tim.check_finish_line() == True:
        for one_car in car_list:
            one_car.increase_speed()


    if tim.check_collision(car_list) == True:
        game_is_on = False

    for one_car in car_list:
        one_car.move_car()

        if one_car.xcor() < -280:
            one_car.teleport(300, random.randint(-250, 250))

screen.exitonclick()
