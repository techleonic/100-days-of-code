import turtle
from turtle import  Turtle, Screen
my_turtle = Turtle()

colors = ["royal blue","lime","light coral","saddle brown","medium slate blue"]
def draw_shape (sides):
    for _ in range(sides):
        my_turtle.forward(100)
        my_turtle.right(360/sides)

sides = 4
i=0
for side in range(sides,9):
    my_turtle.color(colors[i])
    draw_shape(side)
    i+=1


screen = Screen()
screen.exitonclick()