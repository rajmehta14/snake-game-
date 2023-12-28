from turtle import Screen,Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600,height=600)
screen.title("my snake game")
screen.tracer(0)

snake = Snake()
food=Food()
scoreboard=Scoreboard()


screen.listen()

screen.onkey(snake.up,"Up")
screen.onkey(snake.left,"Left")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")











is_game_on=True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>298 or snake.head.ycor()<-298:
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment)<10:
           scoreboard.reset()
           snake.reset()





screen.exitonclick()
