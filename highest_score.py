from turtle import Turtle

ALGNMENT = 'center'
FONT = ("Arial", 24, "normal")

# 5 create a Scoreboard
class HighestScore(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('red')
        with open(file="score.txt",mode="r") as score:
            self.high_score = score.read()
        self.penup()
        self.goto(100,300)
        self.write(arg=f"Highest Score : {self.high_score}",align=ALGNMENT,font=FONT)        
    def highest_score(self, highscore):       
        self.high_score = highscore
        with open(file="score.txt",mode="w") as score:
            score.write(str(self.high_score))
        self.clear()
        self.goto(100,300)
        self.write(arg=f"Highest Score : {self.high_score}",align=ALGNMENT,font=FONT)        