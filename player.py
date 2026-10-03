from turtle import Turtle

STARTING_POSITION = (0, -300)
MOVE_DISTANCE = 20
X_LIMIT = 270


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("triangle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def go_left(self):
        if self.xcor() > -X_LIMIT:
            self.setx(self.xcor() - MOVE_DISTANCE)

    def go_right(self):
        if self.xcor() < X_LIMIT:
            self.setx(self.xcor() + MOVE_DISTANCE)