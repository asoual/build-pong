from turtle import Screen
from table import Table
from paddle import Paddle
from ball import Ball
from score import Score
import time

game_is_on = True
game_paused = True

count = 100
speed = 0.1
def stop_or_resume_game():
    global game_paused
    game_paused = not game_paused
    
screen = Screen()
screen.listen()
screen.setup(width = 1200, height =800)
screen.bgcolor("black")
screen.title(" build pong")
screen.tracer(0)
table = Table()
screen.update()
paddle1 = Paddle(370 , 0)
paddle2 = Paddle(-370 , 0)
ball = Ball()
score = Score()
screen.onkeypress(key="Up",fun=paddle1.move_up)
screen.onkeypress(key="Down",fun=paddle1.move_down)
screen.onkeypress(key="z",fun=paddle2.move_up)
screen.onkeypress(key="s",fun=paddle2.move_down)
screen.onkeypress(stop_or_resume_game, "space")
while game_is_on:
    time.sleep(speed)
    screen.update()
    if not game_paused:
        # detect collisions with walls
        if ball.ycor() > 280 or ball.ycor() < -280: 
            ball.wall_bounce()
            ball.move()
        # detect collisions with paddles
        if (ball.distance(paddle1) < 54 and ball.xcor() > 350) or (ball.distance(paddle2) < 54 and ball.xcor() < -350):
            ball.paddle_bounce() 
            ball.move()   
            count -= 1
            while count !=0:
                print(count)
                speed *= 0.9
                time.sleep(speed)
                break
        # ball out of bound
        if ball.xcor() > 420 :
            ball.ball_reset()
            ball.start_random_direction()
            game_paused = True
            count = 100
            speed = 0.05
            score.update_score(1)
        elif ball.xcor() < -420:
            ball.ball_reset()
            ball.start_random_direction()
            game_paused = True
            count = 100
            speed = 0.05
            score.update_score(2)
        elif score.score1 ==10:
            score.game_over(1)
            game_is_on = False
        elif score.score2 == 10:
            score.game_over(2)
            game_is_on = False
        else:
            ball.move()
screen.exitonclick()