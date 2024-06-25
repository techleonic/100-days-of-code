from turtle import Turtle,Screen
from paddle import  Paddle
from ball import Ball
import  time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


paddle_rigth = Paddle(x_cor=360, y_cor=0)
paddle_left = Paddle(x_cor=-360, y_cor=0)

screen.listen()
screen.onkey(paddle_rigth.go_up,"Up")
screen.onkey(paddle_rigth.go_down,"Down")

screen.onkey(paddle_left.go_up,"w")
screen.onkey(paddle_left.go_down,"s")

ball = Ball()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

screen.exitonclick()