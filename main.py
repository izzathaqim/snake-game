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

screen = turtle.Screen()
screen.listen()
screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Right", fun=snake.move_right)


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move(20)






screen.exitonclick()
