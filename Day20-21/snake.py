from turtle import Turtle

start_position = [(0,0), (-20, 0), (-40, 0)]

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.new_snake()
        self.head = self.segments[0]

    def new_snake(self, shape="square", color="white"):
        for position in start_position:
            self.build_snake(position)
 
    
    def build_snake(self, position):
        seg = Turtle()
        seg.shape("square")
        seg.color("white")
        seg.penup()
        seg.setposition(position)
        self.segments.append(seg)

    def add_segment(self):
        self.build_snake(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            self.segments[seg].goto(self.segments[seg - 1].position())
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
