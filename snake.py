# Import module
import turtle

# Global Variables
# POSITION variables is set as tuples in a list -> coordinate = (x, y)
POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
RIGHT = 0
DOWN = 270


class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for position in POSITION:
            # Call the function add snake and pass the position(coordinate) in POSITION list.
            self.add_snake(position)

    def add_snake(self, position):
        snake = turtle.Turtle(shape="square")
        snake.goto(position)
        snake.color("white")
        snake.penup()
        self.snakes.append(snake)

    def extend_snake(self):
        self.add_snake(self.snakes[-1].position())

    def move(self):
        for snake_number in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[snake_number - 1].xcor()
            new_y = self.snakes[snake_number - 1].ycor()
            self.snakes[snake_number].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)