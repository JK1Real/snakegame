from turtle import Screen, Turtle
import time

from highest_score import HighestScore
from food import Food
from snake import Snake
from scoreboard import Scoreboard
from wall import Wall


screen = Screen()
screen.setup(width=630,height=670)
screen.bgcolor('black')
screen.title('Snake game')

screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
highest_score = HighestScore()

wall = Wall()
wall.createwall()


screen.listen()
screen.onkey(snake.right,'Right')
screen.onkey(snake.left,"Left")
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    
    # 4.Detect collision with food
    if snake.head.distance(food) < 15:

        scoreboard.increase_score()
        food.refresh()
        snake.extend()    
    
    
    # 6.Detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()<-280 or snake.head.ycor()>280 :
#       game_is_on = False
#       scoreboard.gameover()
        if scoreboard.score > int(highest_score.high_score):
            highest_score.highest_score(highscore=scoreboard.score)
        for segs in snake.segments:
            segs.goto(1000,1000)
        snake.reset()
        scoreboard.reset()
        
    # Detect collision with tail
    for segment in  snake.segments[1:]:
        if snake.head.distance(segment) <10:
#            game_is_on = False
#            scoreboard.gameover()
            if scoreboard.score > highest_score.high_score:
                highest_score.highest_score(highscore=scoreboard.score)
            for segs in snake.segments:
                segs.goto(1000,1000)
            snake.reset()
            scoreboard.reset()
            

screen.exitonclick()