from turtle import Turtle

BULLET_SPEED = 20


class Bullet(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=0.2)
        self.penup()
        self.setheading(90)
        self.hideturtle()
        self.active = False

    def fire(self, x, y):
        if not self.active:
            self.goto(x, y + 20)
            self.showturtle()
            self.active = True

    def move(self):
        if self.active:
            self.sety(self.ycor() + BULLET_SPEED)
            if self.ycor() > 340:
                self.reset_bullet()

    def reset_bullet(self):
        self.hideturtle()
        self.active = False