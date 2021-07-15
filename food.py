import turtle
import random


class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh_food()

    def refresh_food(self):
        self.goto(x=random.randint(-250, 250), y=random.randint(-250, 250))

