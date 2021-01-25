from turtle import Turtle, Screen
import random

screen = Screen()
screen.screensize(canvwidth=500, canvheight=400)

race_started = False
finish_line = False

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = {}
y = -100
for color in colors:
    turtles[color] = Turtle(shape="turtle")
    turtles[color].color(color)
    turtles[color].penup()
    turtles[color].setposition(-450, y)
    y += 50
user_bet = screen.textinput(title="Turtle Race Bets", prompt="Which color will win?")

if user_bet:
    race_started = True

while race_started and not finish_line:
    for color in turtles:
        turtles[color].forward(random.randrange(0, 10))
        if turtles[color].xcor() >= 450:
            winner = turtles[color].color()[0]
            finish_line = True
if winner == user_bet:
    print(f"You win! {user_bet} won the race!")
else:
    print(f"You lose! {winner} won the race!")








screen.exitonclick()