import random
from turtle import Turtle

BULLET_SPEED = 10
FIRE_CHANCE = 0.02   # chance per frame
MAX_BULLETS = 3


class AlienBullets:
    def __init__(self):
        self.bullets = []

    def fire(self, aliens):
        if not aliens or len(self.bullets) >= MAX_BULLETS:
            return
        if random.random() > FIRE_CHANCE:
            return

        # bottom-most alien in each column
        columns = {}
        for a in aliens:
            key = round(a.xcor())
            if key not in columns or a.ycor() < columns[key].ycor():
                columns[key] = a
        shooter = random.choice(list(columns.values()))

        b = Turtle("square")
        b.color("red")
        b.shapesize(stretch_wid=0.2, stretch_len=1)
        b.penup()
        b.setheading(270)
        b.goto(shooter.xcor(), shooter.ycor() - 20)
        self.bullets.append(b)

    def move(self):
        for b in self.bullets[:]:
            b.sety(b.ycor() - BULLET_SPEED)
            if b.ycor() < -340:
                self.remove(b)

    def remove(self, b):
        b.hideturtle()
        self.bullets.remove(b)

    def check_player_hit(self, player):
        for b in self.bullets[:]:
            if b.distance(player) < 25:
                self.remove(b)
                return True
        return False