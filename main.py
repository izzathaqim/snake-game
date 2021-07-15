import turtle

x_position = 0
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Games")
snakes = [turtle.Turtle(shape="square") for x in range(3)]


for position in range(3):
    snakes[position].setpos(x=x_position, y=0)
    snakes[position].color("white")
    x_position += 20


screen.exitonclick()
