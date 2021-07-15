# Import module
import turtle
import time
import snake
import food
import scoreboard

# Declare variable to be used on while loop
game_is_on = True

# Screen setup for the game
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
# Turn the turtle animation off
screen.tracer(0)

# Create object from class
snake = snake.Snake()
food = food.Food()
score = scoreboard.ScoreBoard()

# Set keyboard input to control the snake
screen.listen()
screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Right", fun=snake.move_right)

# Play the game using while loop to start and stop the game.
while game_is_on:
    # Turn the animation on
    screen.update()
    # Use the sleep function from time module to delay the refresh rate
    time.sleep(0.1)
    # Use the move method to move the snake
    snake.move()
    # Check whether snake head is close enough to the food to be eaten.
    if snake.head.distance(food) < 15:
        # If the snake had eaten the food, refresh the food location
        food.refresh_food()
        # Increase the score each time
        score.increase_score()
        # Add new turtle to the existing snake
        snake.extend_snake()
    # Check if the snake is within the range of screen
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        # If the snake breach the boundaries set, game over method is call
        score.game_over()
    # Loop through the list of individual turtle location (body of snake) excluding the head.
    for snakes in snake.snakes[1:]:
        # If the head touch any part of the body, game over
        if snake.head.distance(snakes) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()