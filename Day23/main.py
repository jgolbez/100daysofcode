import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("MIDDLE-AGED NORMAL WALKING TURTLE")
screen.listen()
screen.onkey(player.move_up, "Up")
scoreboard = Scoreboard()
carspawn = CarManager()

car_number = 0
current_levelnum = scoreboard.levelnum

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    #Ensure we have adequate cars to squash the turtle
    if car_number < 10:
        car_number += 1
        carspawn.spawn_car()
    #Keep cars moving while game is going, see move_cars method for details
    carspawn.move_cars(current_levelnum)
    #Check if player reached top, cleared level
    if player.ycor() >= 280:
        #Reset turtle, start next level
        player.reset_screen()
        #Add number to next level
        scoreboard.update_scoreboard()
    #Check for turtle squash
    for car in carspawn.carlist:
        if player.distance(car) < 15:
            scoreboard.game_over()
            time.sleep(4)
            exit()



