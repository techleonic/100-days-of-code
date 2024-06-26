import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player =  Player()
screen.listen()
screen.onkey(player.go_up, "Up")
car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    #collition with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

    #detec success
    if player.is_player_finish():
        player.go_to_start()
        car_manager.acelerate()


screen.exitonclick()