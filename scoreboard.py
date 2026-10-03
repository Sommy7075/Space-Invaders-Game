from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.lives = 3
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-280, 310)
        self.write(f"Score: {self.score}", font=("Courier", 18, "normal"))
        self.goto(180, 310)
        self.write(f"Lives: {self.lives}", font=("Courier", 18, "normal"))

    def lose_life(self):
        self.lives -= 1
        self.update_score()

    def add_points(self, points=10):
        self.score += points
        self.update_score()

    def display_message(self, text):
        self.goto(0, 0)
        self.write(text, align="center", font=("Courier", 40, "bold"))


