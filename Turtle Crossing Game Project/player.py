from scoreboard import Scoreboard

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import  Turtle
from scoreboard import Scoreboard

class Player(Scoreboard):

    def __init__(self):
        super().__init__()
        self.main_turtle = Turtle()
        self.main_turtle.penup()
        self.main_turtle.goto(STARTING_POSITION)
        self.main_turtle.showturtle()
        self.main_turtle.shape("turtle")
        self.main_turtle.setheading(90)

    def move_forward(self):
        self.main_turtle.forward(MOVE_DISTANCE)

    def check_finish_line(self):
        if self.main_turtle.ycor() == FINISH_LINE_Y:
            print("You Win")
            self.main_turtle.goto(STARTING_POSITION)
            self.increase_level()
            return True
        else:
            return False

    def check_collision(self,the_list):
        for item in the_list:
            if self.main_turtle.distance(item) < 20:
                self.game_over()
                return True

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over.", align="center", font=("Courier", 24, "normal"))