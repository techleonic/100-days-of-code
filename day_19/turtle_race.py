from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500,height=400)
users_bet=screen.textinput(title="Make your bet", prompt= "Wich turtle will win the race? Enter color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turles = []

def inital():
    for color in colors:
        myturtle = Turtle(shape="turtle")
        myturtle.penup()
        myturtle.color(color)
        turles.append(myturtle)

def start_race():
    i =0
    for turtle in turles:
        turtle.goto(x= -240, y= (-180 -i))
        i-=70

def check_winner(turtle):
    if turtle.xcor() >= 230:
        return False
    else:
        return True

def move_random():
    while True:
        for turtle in turles:
            turtle.forward(random.randint(1, 10))
            if turtle.xcor() >= 230:
                return turtle.pencolor()
        # turtle.forward(random.randint(1, 10))
        # if turtle.xcor() == 230:
        #     turtle.forward(random.randint(1,10))
        # else:
        #     if turtle.color() == users_bet:
        #         print(f"Your win turtle:{turtle.color()}")
        #     else:
        #         print(f"you lose turtle:{turtle.color()}")
        #     break

def check_color(color):
    if users_bet == color:
        print(f"Your win turtle color {color}")
    else:
        print(f"You lose turtle color {color}")

inital()
start_race()
check_color(move_random())
# turtle_red =  Turtle(shape="turtle")
# turtle_red.color("red")
# turtle_red.goto(y=-180,x=-240)

# turtle_blue =  Turtle(shape="Turtle")
# turtle_blue.color("blue")
# turtle_red.goto(y=0,x=-240)
#
# turtle_black =  Turtle()
# turtle_black.color("black")
#
# turtle_green =  Turtle()
# turtle_green.color("green")

screen.exitonclick()