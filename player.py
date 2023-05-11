from turtle import Turtle


class Player:
    def __init__(self):
        self.lives = 3
        self.pen = Turtle()
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(-200, 260)
        self.pen.write(f"Lives: {self.lives}", align="right", font=("Courier", 24, "normal"))

    def update_lives(self):
        self.lives -= 1
        self.pen.clear()
        self.pen.write(f"Lives: {self.lives}", align="right", font=("Courier", 24, "normal"))
        if self.lives == 0:
            self.pen.goto(0,0)
            self.pen.write("GAME OVER!", align="center", font=("Courier", 24, "normal"))
