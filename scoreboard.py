from turtle import Turtle

ALGNMENT = 'center'
FONT = ("Arial", 24, "normal")

# 5 create a Scoreboard
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('red')
        
        self.score=0
        self.high_score = 0
        self.penup()
        self.goto(-100,300)
        self.write(arg=f"score : {self.score}",align=ALGNMENT,font=FONT)
    
    def increase_score(self):
       self.score+=1
       self.clear()
       self.write(arg=f"score : {self.score}",align=ALGNMENT,font=FONT)
    
    def gameover(self):
        self.goto(0,0)
        self.write("Game Over",align=ALGNMENT,font=FONT)

    def reset(self):
        self.score = 0
        self.clear()
        self.write(arg=f"score : {self.score}",align=ALGNMENT,font=FONT)

    def highest_score(self, highscore):
        
        self.high_score = highscore
        self.clear()
        self.goto(100,320)
        self.write(arg=f"Highest Score : {self.highest_score}",align=ALGNMENT,font=FONT)        