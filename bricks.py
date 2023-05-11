from turtle import Turtle
import random
from score import Score


COLOR_LIST = ['royal blue',
              'steel blue', 'light sky blue',
              'violet', 'salmon', 'tomato',
              'sandy brown', 'purple', 'deep pink',
              'medium sea green', 'khaki']


class Brick(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape('square')
        self.color(random.choice(COLOR_LIST))
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.penup()
        self.goto(x_cor, y_cor)
        self.hits = 0  # Keep track of how many times the brick has been hit

    def destroy(self):
        self.goto(x=3000, y=3000)
        self.hideturtle()  # Hide the brick
        self.hits = 0  # Reset the number of hits

    def hit(self):
        self.hits += 1
        if self.hits == 1:
            self.color('white')
        elif self.hits == 2:
            self.goto(-1000, -1000)








