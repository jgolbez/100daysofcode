from turtle import Turtle
font = ("Courier", 16, "normal")
align = "center"
with open("high_score.txt") as file:
    all_time_highscore = int(file.read())

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = all_time_highscore
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 275)
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=align, font=font)

    #def game_over(self):
    #    self.goto(0,0)
    #    self.write("Game Over", align=align, font=font)

    def add_point(self):
        self.score += 1
        self.update_score()


    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()






    
