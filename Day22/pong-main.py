from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

player1 = Paddle((-350,0))
player2 = Paddle((350,0))
playing = True
ball = Ball()
scoreboard = Scoreboard()

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)
screen.listen()
screen.onkey(player1.move_up, "w")
screen.onkey(player1.move_down, "s")
screen.onkey(player2.move_up, "Up")
screen.onkey(player2.move_down, "Down")
while playing:
    screen.update()
    ball.move()
    time.sleep(0.1) 
    #Collide w/ top or bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    #Collide w/ left/right paddle
    if ball.distance(player2) < 50 and ball.xcor() > 320 or ball.distance(player1) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    #Ball is missed by right paddle
    elif ball.xcor() > 380:
        #player 1 point
        player1.setpos(-350, 0)
        player2.setpos(350,0)
        scoreboard.p1point()
        time.sleep(1)
        ball.reset_position()
    #Ball is missed by left paddle
    elif ball.xcor() < -380:
        #player 2 point
        player1.setpos(-350, 0)
        player2.setpos(350,0)
        scoreboard.p2point()
        time.sleep(1)
        ball.reset_position()




screen.exitonclick()
