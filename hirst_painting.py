# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("image.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     tup = (r, g, b)
#     rgb_colors.append(tup)
#
# print(rgb_colors)
import random
import turtle as t

tim = t.Turtle()
t.colormode(255)
colour_list = [(224, 148, 103), (31, 102, 157), (233, 229, 231), (134, 59, 92), (229, 201, 86), (211, 77, 12), (217, 72, 86), (46, 48, 135), (33, 50, 77), (135, 216, 199), (67, 131, 31), (77, 146, 171), (53, 193, 159), (119, 47, 28), (31, 18, 22), (145, 161, 180), (188, 146, 155), (242, 115, 8), (127, 185, 165), (224, 176, 166), (209, 89, 65), (45, 24, 20), (252, 204, 1), (108, 121, 161), (215, 176, 182), (183, 188, 209), (125, 43, 67)]

tim.pensize(10)
tim.speed(10)

pos = 1
x_var = -300
y_var = -300
# for num in range(1, 11):
tim.penup()
tim.hideturtle()
tim.setposition(x_var, y_var)
dots = 0
for _ in range(100):
    curr_col = random.choice(colour_list)
    tim.dot(20, curr_col)
    tim.penup()
    tim.forward(50)
    dots += 1

    if dots == 10:
        tim.penup()
        y_var += 50
        tim.setposition(x_var, y_var)
        dots = 0

screen = t.Screen()
screen.exitonclick()