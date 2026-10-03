from turtle import Turtle

BARRIER_COUNT = 4
BARRIER_Y = -200
BLOCK_SIZE = 10
ROWS = 3
COLS = 6


class Barriers:
    def __init__(self):
        self.blocks = []
        self.create_barriers()

    def create_barriers(self):
        spacing = 600 / BARRIER_COUNT
        for i in range(BARRIER_COUNT):
            center_x = -225 + i * spacing
            for row in range(ROWS):
                for col in range(COLS):
                    block = Turtle("square")
                    block.color("cyan")
                    block.shapesize(0.5, 0.5)
                    block.penup()
                    x = center_x - (COLS - 1) * BLOCK_SIZE / 2 + col * BLOCK_SIZE
                    y = BARRIER_Y + row * BLOCK_SIZE
                    block.goto(x, y)
                    self.blocks.append(block)

    def check_bullet_hit(self, bullet):
        if not bullet.active:
            return
        for block in self.blocks:
            if block.distance(bullet) < 15:
                block.hideturtle()
                self.blocks.remove(block)
                bullet.reset_bullet()
                return

    def check_alien_bullets(self, alien_bullets):
        for b in alien_bullets.bullets[:]:
            for block in self.blocks:
                if block.distance(b) < 15:
                    block.hideturtle()
                    self.blocks.remove(block)
                    alien_bullets.remove(b)
                    break