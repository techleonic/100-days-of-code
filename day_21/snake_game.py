from turtle import Screen
import time
from food import Food
from snake import Snake
from scoreboard import ScoreBoard

screen =  Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

score = ScoreBoard()
game_is_one = True

while game_is_one :
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detec collision with food
    if  snake.head.distance(food) < 15 :
        food.refersh()
        snake.extend()
        score.update_score()

    #DETEC COLITION WITH WALL
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_one = False
        score.game_over()

    #detec head collision eith tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_one = False
            score.game_over()

screen.exitonclick()