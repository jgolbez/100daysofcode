import turtle as t
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("green")
colors = ["red", "green", "blue", "yellow", "teal", "peru", "medium orchid", "gold", "DarkRed", "cornflower blue", "medium spring green"]
heading = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

"""[Draw a Box]"""
#for _ in range(4):
#    tim.forward(100)
#    tim.rt(90)

"""[Draw Dotted Lines]"""
#tim.setpos(-10, y=0)
#for _ in range(15):
#    tim.forward(10)
#    tim.pu()
#    tim.forward(10)
#    tim.pd()



"""[Draw Shapes On Top of Each Other w/ Random Color]
angles = {
    3 : 120, 
    4: 90, 
    5: 72, 
    6: 60, 
    7: 51, 
    8: 45,
    9: 40,
    10: 36,
}
for sides, angle in angles.items():
    tim.color(random.choice(colors))
    while sides > 0:
        tim.forward(100)
        tim.rt(angle)
        sides -= 1
"""

"""[Random Walk]

tim.pensize(8)
tim.hideturtle()
while True:
    tim.color(random.choice(colors))
    tim.setheading(random.choice(heading))
    tim.forward(25)
# Randomize color with random color function
t.colormode(255)
tim.pensize(8)
tim.hideturtle()
while True:
    tim.color(random_color())
    tim.forward(25)
    tim.setheading(random.choice(heading))
"""


"""Draw a Spirograph
tim.speed("fastest")
tim.hideturtle()

def draw_spirograph(gap):
    for _ in range(int(360 / gap)):
        tim.color(random.choice(colors))
        tim.circle(90)
        tim.setheading(int(tim.heading()) + gap)
 #   if tim.heading >= 360:
 #       circledraw = False
draw_spirograph(5)

"""











screen = Screen()
screen.exitonclick()

