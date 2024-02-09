from turtle import Turtle

WIDTH = 4
LENGTH = 1
class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(WIDTH, LENGTH)
        self.penup()
        self.goto(x_pos,y_pos)

    def move_up(self):
        new_y = self.ycor() + 20
        if new_y < 280:
            self.sety(new_y)
    
    def move_down(self):
        new_y = self.ycor() - 20
        if new_y > -280:
            self.sety(new_y)
    