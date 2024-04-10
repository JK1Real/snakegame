from turtle import Turtle

class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
    
    def createwall(self):
        self.penup()
        self.color('red')
        self.pen(pensize=10)

        self.goto(x=(-290,290))
        self.pendown()
        for _ in range(4):
            self.forward(580)
            self.right(90)
            