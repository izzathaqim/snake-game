import turtle
import time

x_position = 0
game_is_on = True

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Games")
screen.tracer(0)

snakes = [turtle.Turtle(shape="square") for x in range(3)]
positions = [(0, 0), (-20, 0), (-40, 0)]

for position in positions:
    location = positions.index(position)
    snakes[location].goto(position)
    snakes[location].color("white")
    snakes[location].penup()

while game_is_on:
    screen.update()
    time.sleep(0.5)

    for snake_number in range(len(snakes) - 1, 0, -1):
        new_x = snakes[snake_number - 1].xcor()
        new_y = snakes[snake_number - 1].ycor()
        snakes[snake_number].goto(x=new_x, y=new_y)
    snakes[0].forward(20)




screen.exitonclick()
