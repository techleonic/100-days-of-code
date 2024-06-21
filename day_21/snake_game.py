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

while True :
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detec collision with food
    if  snake.segments[-1].distance(food) < 15 :
        food.refersh()
        score.update_score()



screen.exitonclick()