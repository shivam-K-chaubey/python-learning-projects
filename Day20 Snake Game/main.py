import time
from scoreboard import Score
from turtle import Screen
from snake import Snake
from food import Food


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
score = Score()
score.display_score()
food.refresh()


screen.listen()
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.up ,key="Up")
screen.onkey(fun=snake.down, key="Down")

while True:
    screen.update()
    time.sleep(0.12)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
    snake_x = snake.head.xcor()
    snake_y = snake.head.ycor()
    if snake_x > 280 or snake_x < -280 or snake_y > 250 or snake_y < -280:
        score.game_over()
        break
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.game_over()
            break

screen.exitonclick()
