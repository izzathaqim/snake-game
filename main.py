import turtle
import time
import snake


x_position = 0
game_is_on = True

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Games")
screen.tracer(0)

snake = snake.Snake()
snake.control()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move(20)






screen.exitonclick()
