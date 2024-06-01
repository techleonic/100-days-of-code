import turtle
import turtle
import random


my_turtle = turtle.Turtle()
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return  random_color

turtle.colormode(255)
my_turtle.color()
my_turtle.speed("fastest")

def draw_spirograhp(gap_size):
    for _ in range(int(360/ gap_size)):
        my_turtle.color(random_color())
        my_turtle.circle(100)
        my_turtle.setheading(my_turtle.heading() + gap_size)

draw_spirograhp(5)
screen = turtle.Screen()
screen.exitonclick()