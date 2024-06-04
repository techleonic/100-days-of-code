import turtle
from turtle import Turtle, Screen
import random

my_turtle = Turtle()
list_colors = [(252, 138, 52), (49, 171, 90), (120, 185, 140),  (249, 75, 110)]
x_len = 10
y_len = 10
dir =5
turtle.colormode(255)
my_turtle.pu()
def color_random(my_turtle):
    my_turtle.color(random.choice(list_colors))


# color_random(my_turtle)
# my_turtle.dot(10)
# print(my_turtle)
y_jump = 30
for i in range(y_len):
    for i in range(x_len):
        color_random(my_turtle)
        my_turtle.forward(30)
        my_turtle.dot(15)
    my_turtle.setx(0)
    my_turtle.sety(y_jump)
    y_jump+=30


# for i in range(1, x_len):
#     color_random(my_turtle)
#     my_turtle.setx(my_turtle.xcor()+dir)
#     my_turtle.dot(15)
#     dir+=dir

screen =  Screen()
screen.exitonclick()