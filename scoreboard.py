from turtle import Turtle, fillcolor

ALIGMENT = "center"
FONT = ("Calibri", 19, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score.txt") as data:
           self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score:{self.highscore}", align=ALIGMENT, font=FONT)   

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("score.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

    def counter_score(self):
        self.score += 1
        self.update_scoreboard()
    
