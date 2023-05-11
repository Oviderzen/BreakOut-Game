from turtle import Turtle


class Score:
    def __init__(self):
        self.score = 0
        self.pen = Turtle()
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(200, 260)
        self.pen.write("Score: {}".format(self.score), align="left", font=("Courier", 24, "normal"))


    def update_score(self, points):
        self.score += points
        self.pen.clear()
        self.pen.write("Score: {}".format(self.score), align="center", font=("Courier", 24, "normal"))
        if self.score == 3000:
            self.pen.speed(0)
            self.pen.color("white")
            self.pen.penup()
            self.pen.hideturtle()
            self.pen.goto(0, 0)
            self.pen.write(f"YOU WIN!", align="right", font=("Courier", 24, "normal"))



