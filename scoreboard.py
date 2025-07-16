from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self, x_cord, y_cord):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.setposition(x_cord, y_cord)
        self.write(f"Score: {self.score}", font=("Courier", 20, "normal"))
        self.hideturtle()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", font=("Courier", 20, "normal"))







    # def __init__(self, side):
    #     super().__init__()
    #     self.left_score = 0
    #     self.right_score = 0
    #     self.color("white")
    #     self.penup()
    #     if side == "right":
    #         self.setposition(200, 260)
    #         self.write(f"Score: {self.left_score}", align=side, font = ("Courier", 20, "normal"))
    #         self.hideturtle()
    #
    #     if side == "left":
    #         self.setposition(-200, 260)
    #         self.write(f"Score: {self.right_score}", align=side, font = ("Courier", 20, "normal"))
    #         self.hideturtle()
    #
    # def increase_left(self):
    #     self.left_score += 1
    #
    # def increase_right(self):
    #     self.right_score += 1
