import turtle
from turtle import  Turtle,Screen
import random
my_turtle = Turtle ()

directions= [0,90,180,270]
colors = ["royal blue","lime","light coral","saddle brown","medium slate blue"]
my_turtle.pensize(15)
my_turtle.speed(20)
for _ in range(100):
    my_turtle.color(random.choice(colors))
    my_turtle.forward(50)
    my_turtle.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()