from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-275, 250)
        self.levelnum = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.levelnum += 1
        self.score = f"Level: {self.levelnum}"
        self.write(self.score, align="left", font=(FONT))

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=(FONT))





