import turtle
from turtle import  Turtle,Screen
import random
my_turtle = Turtle ()
turtle.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return  random_color


directions= [0,90,180,270]


my_turtle.pensize(15)
my_turtle.speed(20)


for _ in range(100):
    my_turtle.color(random_color())
    my_turtle.forward(50)
    my_turtle.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()