from turtle import Turtle
from turtle import Screen
screen = Screen()
STARTING_POSITION  = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20

Left = 180
Right = 0 
Up = 90
Down = 270

class Snake:

    def __init__(self) :
        # 1.create a snake body

        self.segments =[]
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

        screen.update()

        self.head = self.segments[0]

    def add_segment(self,position):
            segment_new = Turtle(shape='square')
            segment_new.color('white')
            segment_new.penup()
            segment_new.goto(position)
            self.segments.append(segment_new)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        self.segments =[]
        self.create_snake()



    def move(self):
        # 2. Move the snake
            for seg_num in range(len(self.segments)-1,0,-1):
                new_x = self.segments[seg_num-1].xcor()
                new_y = self.segments[seg_num-1].ycor()
                self.segments[seg_num].goto(new_x,new_y)
            self.segments[0].forward(MOVE_DISTANCE)



    def left(self):
         if self.head.heading() !=Right:
             self.head.setheading(Left)
    
    def right(self):
         if self.head.heading() !=Left:
            self.head.setheading(Right)

    def up(self):
         if self.head.heading() !=Down:
            self.head.setheading(Up)

    def down(self):
         if self.head.heading() !=Up:
             self.head.setheading(Down)

    