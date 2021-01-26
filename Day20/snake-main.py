from turtle import Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snakes on a Flat, Black Plane")
screen.tracer(0)
import time

racing = True

snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


while racing:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()



























screen.exitonclick()
