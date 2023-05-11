import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from bricks import Brick
from player import Player

# Create the screen
screen = Screen()
screen.setup(width=1200, height=600)
screen.bgcolor('black')
screen.title('BreakOut')
screen.tracer(0)

turtle = Turtle()
paddle = Paddle()

screen.listen()
screen.onkeypress(key='Left', fun=paddle.move_left)
screen.onkeypress(key='Right', fun=paddle.move_right)

ball = Ball()
player = Player()


game_on = True


# Create a list to hold all the bricks
bricks = []
# Create the bricks and add them to the list
for row in range(3):
    for col in range(10):
        brick = Brick(-450 + col * 100, 250 - row * 50)
        bricks.append(brick)

def check_wall_collision():
    global ball, game_on
    # Detect ball collision with walls
    if ball.xcor() < -580 or ball.xcor() > 570:
        ball.bounce_x()

    if ball.ycor() > 270:
        ball.bounce_y()

    if ball.ycor() < -280:
        player.update_lives()
        ball.reset_pos()


def check_paddle_collision():
    global paddle, ball
    # Detect collision between the paddle and the ball
    if ball.distance(paddle) < 100 and ball.ycor() < -250:
        ball.bounce_y()
        return


def check_brick_collision():
    global ball, bricks
    # Detect collision between the ball and the bricks
    for brick in bricks:
        if ball.distance(brick) < 40:
            ball.bounce_y()
            brick.hit()


while game_on:
    screen.update()
    time.sleep(0.01)
    ball.move()
    check_wall_collision()
    check_paddle_collision()
    check_brick_collision()
    if player.lives == 0:
        print('Game Over.')
        game_on = False

screen.mainloop()