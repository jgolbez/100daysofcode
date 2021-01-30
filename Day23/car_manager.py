from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.carlist = []
    
    def spawn_car(self):
        car = Turtle()
        car.shape("square")
        car.resizemode("user")
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.color(random.choice(COLORS))
        car.penup()
        #Every time we create a new car, stagger it and randomize it
        car.setposition(random.randint(-200, 280), random.randint(-240, 240))
        car.setheading(180)
        self.carlist.append(car)

    def move_cars(self, levelnum):
        # Check if car has left the screen, respawn on right side in new position
        for car in self.carlist:
            if car.xcor() < -280:
                car.setposition(random.randint(255, 280), random.randint(-240, 240))
        #Otherwise keep moving, speed up per level cleared
            else:
                car.forward(5 + (10 * levelnum))


