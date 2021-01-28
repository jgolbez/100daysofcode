from turtle import Turtle
font = ("Courier", 16, "normal")
align = "center"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 275)
        self.write(f"Score: {self.score}", align=align, font=font)
#        self.clear()


    
    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=align, font=font)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align=align, font=font)



    
