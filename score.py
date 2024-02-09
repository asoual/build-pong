from turtle import Turtle 

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-350,320)
        self.write(f"Player 1: {self.score1}", font=("Verdana", 15, "normal"))
        self.goto(250,320)
        self.write(f"Player 2: {self.score2}", font=("Verdana", 15, "normal"))

    def update_score(self, player):
        if player == 1:
            self.score1 += 1
            self.clear()
            self.goto(-350,320)
            self.write(f"Player 1: {self.score1}", font=("Verdana", 15, "normal"))
            self.goto(250,320)
            self.write(f"Player 2: {self.score2}", font=("Verdana", 15, "normal"))
        elif player == 2:
            self.score2 += 1
            self.clear()
            self.goto(-350,320)
            self.write(f"Player 1: {self.score1}", font=("Verdana", 15, "normal"))
            self.goto(250,320)
            self.write(f"Player 2: {self.score2}", font=("Verdana", 15, "normal"))
        
    def game_over(self,player):
        self.goto(0,80)
        self.write(f"Player {player} Won the game ",align= "center",font=("Verdana", 15, "normal"))
