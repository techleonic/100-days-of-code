import turtle as turtle_module
import random

my_turtle = turtle_module.Turtle()
turtle_module.colormode(255)
list_colors = [(252, 138, 52), (49, 171, 90), (120, 185, 140),  (249, 75, 110)]
my_turtle.penup()
my_turtle.setheading(225)
my_turtle.forward(300)
my_turtle.setheading(0)
number_of_dots = 100
my_turtle.speed("fastest")


for dot_count in range(1, number_of_dots+1):
    my_turtle.dot(20, random.choice(list_colors))
    my_turtle.forward(50)
    if dot_count % 10 == 0:
        my_turtle.setheading(90)
        my_turtle.forward(50)
        my_turtle.setheading(180)
        my_turtle.forward(500)
        my_turtle.setheading(0)





screen = turtle_module.Screen()
screen.exitonclick()
