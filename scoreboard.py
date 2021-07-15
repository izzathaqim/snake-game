import turtle


class ScoreBoard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.print_score()

    def print_score(self):
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.write(arg=f"Score: {self.score}", font=("Ubuntu", 15, "normal"), align="center")
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.print_score()

    def game_over(self):
        self.clear()
        self.color("white")
        self.goto(x=0, y=0)
        self.write(arg=f"Game Over. Your Score is {self.score}", font=("Ubuntu", 20, "bold"), align="center")
        self.hideturtle()

