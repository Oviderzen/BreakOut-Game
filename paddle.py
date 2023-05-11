from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len=8)
        self.penup()
        self.goto(x=0, y=-280)

    def move_left(self):
        if self.xcor() < -550:
            self.backward(0)
        else:
            self.backward(50)

    def move_right(self):
        if self.xcor() > 500:
            self.forward(0)
        else:
            self.forward(50)