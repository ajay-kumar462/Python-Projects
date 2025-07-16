from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
heights = [-90, -60, -30, 0, 30, 60]
colours = ["red", "blue", "green", "orange", "yellow", "violet"]
user_bet = screen.textinput(title="Make a bet.", prompt="Select a color you think will win.")
is_on = False
all_turtles = []
for num in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[num])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=heights[num])
    all_turtles.append(new_turtle)

if user_bet:
    is_on = True

while is_on:
    for each_turtle in all_turtles:
        distance = random.randint(0, 10)
        each_turtle.forward(distance)
        if each_turtle.xcor() > 230:
            winning_color = each_turtle.pencolor()
            is_on = False
            if user_bet == winning_color:
                print(f"You win! The winner is {winning_color}")
            else:
                print(f"You lose! The winner is {winning_color}")
screen.exitonclick()





#My method

# tim = Turtle(shape="turtle")
# tim.penup()
# tom = Turtle(shape="turtle")
# tom.penup()
# jam = Turtle(shape="turtle")
# jam.penup()
# jon = Turtle(shape="turtle")
# jon.penup()
# pan = Turtle(shape="turtle")
# pan.penup()
# pon = Turtle(shape="turtle")
# pon.penup()
# screen = Screen()
#
# user_bet = screen.textinput(title="Make your bet.", prompt="Select a colour of turtle you think would win.")
# print(user_bet)
# colours = ["red", "blue", "green", "orange", "yellow", "violet"]
# turt_names = [tim, tom, jam, jon, pan, pon]
#
# x_val = -230
# y_val = -100
# loop = 0
# def set_start_positions(t_name):
#     global x_val, y_val
#     t_name.goto(x= x_val, y=y_val)
#     y_val += 50
#
# for name in turt_names:
#     set_start_positions(name)
#     name.color(colours[loop])
#     loop += 1