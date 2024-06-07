from turtle import  Turtle, Screen

my_turtle =  Turtle()
screen =  Screen()
screen.listen()
def move_forwads():
    my_turtle.forward(10)

def move_backwards():
    my_turtle.backward(10)

def move_counter_clockwise():
    my_turtle.setheading(my_turtle.heading() + 10)

def move_clockwise():
    my_turtle.setheading(my_turtle.heading() -10)
def clear_screen():
    my_turtle.clear()
    my_turtle.reset()


screen.onkey(fun= move_forwads,key="w")
screen.onkey(fun= move_backwards,key="s")
screen.onkey(fun= move_counter_clockwise,key="a")
screen.onkey(fun= move_clockwise,key="d")
screen.onkey(fun= clear_screen,key="c")


screen.exitonclick()