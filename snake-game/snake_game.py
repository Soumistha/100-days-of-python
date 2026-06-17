import time
import turtle as t
import random
from snake import Snake
from food import Food
from scoreboard import Score


screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("My snake Game")
screen.tracer(0)

#bella.shape("turtle") #changes the shape from arrow to turtle
#t.colormode(255)

# bella = t.Turtle("square")
# bella.color("white")

# seg1 = t.Turtle("square")
# seg1.color("white")
# seg1.goto(-20, 0)

# seg2 = t.Turtle("square")
# seg2.color("white")
# seg2.goto(-40, 0)
snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:  
    screen.update()
    time.sleep(0.1)

    snake.move()

    #collison with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()
    
    #detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score.goto(0, 0)
        score.write("Game Over", align="center", font=("Arial", 24, "normal"))
    
    #detect collision with tail
    for segment in snake.seg[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.goto(0, 0)
            score.write("Game Over", align="center", font=("Arial", 24, "normal"))
    

screen.listen()

screen.exitonclick()