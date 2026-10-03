import time
from turtle import Screen
from player import Player
from bullet import Bullet
from aliens import AlienFleet
from barriers import Barriers
from scoreboard import Scoreboard
from alien_bullets import AlienBullets



screen = Screen()
screen.setup(width=600, height=700)
screen.bgcolor("black")
screen.title("Space Invaders")
screen.tracer(0)

player = Player()
fleet = AlienFleet()
barriers = Barriers()
alien_bullets = AlienBullets()
bullet = Bullet()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.go_left, "Left")
screen.onkeypress(player.go_right, "Right")
screen.onkeypress(lambda: bullet.fire(player.xcor(), player.ycor()), "space")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.02)
    bullet.move()
    fleet.move()
    alien_bullets.fire(fleet.aliens)
    alien_bullets.move()

    if fleet.check_bullet_hit(bullet):
        scoreboard.add_points()
    barriers.check_bullet_hit(bullet)
    barriers.check_alien_bullets(alien_bullets)

    if alien_bullets.check_player_hit(player):
        scoreboard.lose_life()

    if scoreboard.lives == 0 or fleet.reached_player(player):
        game_is_on = False
        scoreboard.display_message("GAME OVER")
    elif not fleet.aliens:
        game_is_on = False
        scoreboard.display_message("YOU WIN!")

screen.update()
screen.exitonclick()

screen.update()
screen.exitonclick()