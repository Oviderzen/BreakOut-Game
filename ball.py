from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.y_move_dist = 4
        self.x_move_dist = 4


    def move(self):
        new_x = self.xcor() + self.x_move_dist
        new_y = self.ycor() + self.y_move_dist
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move_dist *= -1

    def bounce_y(self):
        self.y_move_dist *= -1

    def reset_pos(self):
        self.hideturtle()
        self.goto(x=0, y=-200)
        self.showturtle()
        self.bounce_y()