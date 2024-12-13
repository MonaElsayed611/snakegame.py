from turtle import Turtle, Screen
from snake import Snake
import time
from food import Food
from scoreboard import Score_board
window = Screen ()
window.bgcolor("black")
window.setup(width = 600, height = 600)
window.title ("Snake Game")
window.tracer(0)


snake = Snake()
food = Food ()
score = Score_board()

game_on = True 
while game_on :
    snake.move()
    window.update()
    time.sleep(0.1)
    window.listen()
    window.onkey(snake.up,"Up")
    window.onkey(snake.down,"Down")
    window.onkey(snake.right,"Right")
    window.onkey(snake.left,"Left")
    if snake.head.distance(food) < 15:
        food.display()
        snake.extend()
        score.update_score()

    if snake.head.xcor() < -275 or snake.head.xcor() > 275 or snake.head.ycor() < -275 or snake.head.ycor() > 275: 
        game_on = False
        score.game_over()
    for segment in snake.turtles[:-1]:      
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()





window.exitonclick()