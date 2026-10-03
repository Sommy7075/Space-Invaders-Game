import time
from turtle import Turtle

ROWS = 4
COLS = 8
X_START = -210
Y_START = 250
X_GAP = 60
Y_GAP = 50
COLORS = ["red", "orange", "yellow", "green"]


class AlienFleet:
    def __init__(self):
        self.aliens = []
        self.direction = 1
        self.step = 15
        self.drop = 20
        self.move_delay = 0.5
        self.last_move = time.time()
        self.create_fleet()

    def create_fleet(self):
        for row in range(ROWS):
            for col in range(COLS):
                alien = Turtle("square")
                alien.color(COLORS[row])
                alien.shapesize(stretch_wid=1, stretch_len=1.5)
                alien.penup()
                alien.goto(X_START + col * X_GAP, Y_START - row * Y_GAP)
                self.aliens.append(alien)

    def move(self):
        if time.time() - self.last_move < self.move_delay:
            return
        self.last_move = time.time()

        hit_edge = any(
            abs(a.xcor() + self.direction * self.step) > 270 for a in self.aliens
        )
        if hit_edge:
            self.direction *= -1
            for a in self.aliens:
                a.sety(a.ycor() - self.drop)
        else:
            for a in self.aliens:
                a.setx(a.xcor() + self.direction * self.step)

    def check_bullet_hit(self, bullet):
        if not bullet.active:
            return False
        for alien in self.aliens:
            if alien.distance(bullet) < 25:
                alien.hideturtle()
                self.aliens.remove(alien)
                self.move_delay = max(0.1, self.move_delay * 0.97)
                bullet.reset_bullet()
                return True
        return False

    def reached_player(self, player):
        for alien in self.aliens:
            if alien.distance(player) < 30 or alien.ycor() <= player.ycor() + 30:
                return True
        return False