from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Score()

screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    if (r_paddle.distance(ball) < 60 and ball.xcor() > 320) or (l_paddle.distance(ball) < 60 and ball.xcor() < -320):
        ball.x_bounce()

    elif ball.xcor() > 380:
        scoreboard.l_score_count()
        ball.reset_coordinates()

    elif ball.xcor() < -380:
        scoreboard.r_score_count()
        ball.reset_coordinates()

    if scoreboard.l_score == 5 or scoreboard.r_score == 5:
        game_on = False

scoreboard.game_finished()

screen.exitonclick()
