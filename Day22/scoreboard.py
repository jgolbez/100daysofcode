from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.p1_score = 0
        self.p2_score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.p1_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.p2_score, align="center", font=("Courier", 80, "normal"))

    def p1point(self):
        self.p1_score += 1
        self.update_scoreboard()

    def p2point(self):
        self.p2_score += 1
        self.update_scoreboard()
