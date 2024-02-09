from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        # self.x_move = 10
        # self.y_move = 10
        self.start_random_direction()
        
    def start_random_direction(self):
        excluded_ranges = [(0,10), (70, 110), (160, 200), (250, 290),(350,360)]  
        while True:
            rand_angle = random.randrange(0, 360, 40)
            if all(start > rand_angle or rand_angle > end for start, end in excluded_ranges):
                break
        self.setheading(rand_angle)    
    def move(self):
        self.forward(10)  
        
    def wall_bounce(self):
        self.setheading(360 - self.heading())
        
    def paddle_bounce(self):
        self.setheading(180 - self.heading())
        
    def ball_reset(self):
        self.goto(0, 0)
        self.stop_ball()

    def stop_ball(self):
        self.x_move = 0
        self.y_move = 0