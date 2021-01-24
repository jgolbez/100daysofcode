###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
"""[generate color palette from image]
    
import colorgram

colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)
"""

from color_list import colors
from turtle import Turtle, Screen
import turtle as t
import random

t.colormode(255)
screen = Screen()
tim = Turtle()

#Create Dot
def mark_dot():
    color_choice = random.choice(colors)
    tim.dot(20, color_choice)

#Move to next row and orient
def reorient(heading):
    if heading == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(50)
    else:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(0)
        tim.forward(50)


#Start lower left
tim.penup()
tim.setheading(225)
tim.forward(350)
tim.setheading(0)

#Draw Line of dots
for _ in range(10):
    for _ in range(10):
        mark_dot()
        tim.penup()
        tim.forward(50)
    heading = tim.heading()    
    reorient(heading) 


screen.exitonclick()
