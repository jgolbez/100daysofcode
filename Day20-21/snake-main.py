from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snakes on a Flat, Black Plane")
screen.tracer(0)

scoreboard = Scoreboard()

eating = True

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


while eating:
    screen.update()
    time.sleep(0.1)
    snake.move()
# Detect food collision
    if snake.head.distance(food) < 15:
        food.respawn()
        scoreboard.update_score()
        snake.add_segment()
#Detect wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        eating = False
        scoreboard.game_over()
#Detect snake body collision
    for segment in snake.segments[1:]:
#        if segment == snake.head:
#            pass
        if snake.head.distance(segment) < 10:
            eating = False
            scoreboard.game_over()

screen.exitonclick()



























screen.exitonclick()
