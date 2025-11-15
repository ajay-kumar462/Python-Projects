COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1

from turtle import Turtle, Screen
import random, time
from player import Player

class CarManager(Turtle):

    def  __init__(self):
        super().__init__()
        self.shape("square")
        self.setheading(180)
        self.shapesize(1, 2)
        self.add_color()

    def move_car(self):
        self.penup()
        self.forward(STARTING_MOVE_DISTANCE)

    def add_color(self):
        self.color(random.choice(COLORS))

    def increase_speed(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT




