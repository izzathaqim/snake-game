import turtle

# Global Variables
POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.move_up()
        self.move_down()
        self.move_left()
        self.move_right()

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

    def control(self):
        screen = turtle.Screen()
        screen.listen()
        screen.onkey(key="Up", fun=self.move_up)
        screen.onkey(key="Down", fun=self.move_down)
        screen.onkey(key="Left", fun=self.move_left)
        screen.onkey(key="Right", fun=self.move_right)

    def move_up(self):
        self.snakes[0].setheading(90)
        self.snakes[0].forward(20)

    def move_down(self):
        self.snakes[0].setheading(270)
        self.snakes[0].forward(20)

    def move_right(self):
        self.snakes[0].setheading(0)
        self.snakes[0].forward(20)

    def move_left(self):
        self.snakes[0].setheading(180)
        self.snakes[0].forward(20)
