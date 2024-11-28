from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height= 600)
screen.bgcolor("black")
screen.title("My Snake Game")

screen.tracer(0) #we turn off the tracer for the animattion to work.

snake = Snake()
food = Food()
board = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update() #show the screen in it's updated mode
    time.sleep(0.1) #delay the animation by 0.1 seconds each time 
   
    snake.move()
    
    #Detect collision with food 
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        board.get_score()
        
    #Detect collision with wall 
    if snake.head.xcor() > 295 or snake.head.ycor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() < -295:
        board.reset()
        snake.reset() 
        
    #Detect collision with tail 
    for turtle in snake.turtles[1:]: # we should skip the head (the first turtle) beacouse we are checkig the head
        if snake.head.distance(turtle) < 10:
            board.reset()
            snake.reset() 
                







screen.exitonclick()