from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Screen settings
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right = (350, 0)
left = (-350, 0)

r_paddle = Paddle(right)
l_paddle = Paddle(left)

ball = Ball()

score_left = Scoreboard(100, 260)
score_right = Scoreboard(-250, 260)

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()

    ball.move()

    # Detection if ball has collided with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detection if ball has collided with either of the paddle
    if ball.distance(r_paddle) <= 50 and ball.xcor() > 320 or ball.distance(l_paddle) <= 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        score_right.increase_score()
        ball.ball_reset()

    elif ball.xcor() < -380:
        score_left.increase_score()
        ball.ball_reset()




screen.exitonclick()
