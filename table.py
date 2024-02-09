from turtle import Turtle

class Table(Turtle):
    def __init__(self):
        super().__init__()
        # self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-400,-300)
        self.pendown()
        self.goto(400,-300)
        self.goto(400,300)
        self.goto(-400,300)
        self.goto(-400,-300)
        self.penup()
        self.goto(0,-300)
        self.left(90)
        while self.ycor() < 300:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(10)
            