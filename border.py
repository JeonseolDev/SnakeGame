from turtle import Turtle
BORDER_POSITIONS = [(-300, -300), (-300, 300), (300, 300), (300, -300), (-300, -300)]


class Border(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(BORDER_POSITIONS[0])
        self.pendown()
        self.goto(BORDER_POSITIONS[1])
        self.goto(BORDER_POSITIONS[2])
        self.goto(BORDER_POSITIONS[3])
        self.goto(BORDER_POSITIONS[4])