import turtle

# Global Variables
POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()

    def create_snake(self):
        for position in POSITION:
            snake = turtle.Turtle(shape="square")
            snake.goto(position)
            snake.color("white")
            snake.penup()
            self.snakes.append(snake)

    def move(self, MOVE_DISTANCE):
        for snake_number in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[snake_number - 1].xcor()
            new_y = self.snakes[snake_number - 1].ycor()
            self.snakes[snake_number].goto(x=new_x, y=new_y)
        self.snakes[0].forward(MOVE_DISTANCE)
