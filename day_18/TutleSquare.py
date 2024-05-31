import math as m #su cam inmport an put a alias name
m.sin(8) #then you can use it with the alias name
from turtle import Turtle,Screen


turtle =  Turtle()
turtle.color("red")

#position = turtle.pos()

for i in range(4):
    turtle.right(90)
    turtle.forward(90)


screen = Screen()
screen.exitonclick()



