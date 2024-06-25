from turtle import Turtle,Screen
from paddle import  Paddle
from ball import Ball
import  time
from  scoreboard import Scoreboard

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
score = Scoreboard()
speed = 0.1


game_is_on = True
while game_is_on:
    time.sleep(speed)
    screen.update()
    ball.move()

    #wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #paddle collition
    if ball.distance(paddle_rigth) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.y_move *= 1.005
        ball.x_move *= 1.005
        ball.bounce_x()
        print(f"{ball.x_move}")

    #detect right paddel miss it
    if ball.xcor() > 380:
        ball.reset()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset()
        score.r_point()

screen.exitonclick()