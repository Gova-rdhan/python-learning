from turtle import Screen
from snake import Snake
from foood_generator import Food
from scoreboard import Score
import time
cordiantes = 290
snake = Snake()
food = Food()
scoreboard = Score()
sc = Screen()
sc.bgcolor("black")
sc.setup(width=600,height=600)
sc.title("snake game!!!!!!!!")
sc.tracer(0)
sc.listen()
sc.onkey(snake.go_up,"Up")
sc.onkey(snake.go_down,'Down')
sc.onkey(snake.left_side,'Left')
sc.onkey(snake.right_side,'Right')
snake.go_up()
snake.left_side()
snake.right_side()
snake.go_down()
food.food_refresh()
while snake.is_start:
    sc.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 20:
        scoreboard.increase_score()
        food.food_refresh()
        snake.extend()
    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        scoreboard.reset_score()
        snake.reset_snake()

    for position in snake.snake[1:]:
        if snake.head.distance(position.position()) < 5:
            scoreboard.reset_score()
            snake.reset_snake()



sc.exitonclick()