import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Function to modify the screen settings
def modify_screen():
    screen.setup(width=600, height=600)  # Set the window size to 600x600 pixels
    screen.bgcolor("black")  # Set the background color to black
    screen.tracer(0)  # Turn off automatic screen updates for smoother animations

# Function to listen for key presses
def listen_key():
    screen.listen()  # Start listening for key presses
    screen.onkey(fun=player.move_up, key="Up")  # Call player's move_up function when "Up" key is pressed

# Set up the game screen
screen = Screen()
modify_screen()

# Initialize the player, car manager, and scoreboard objects
player = Player()
cars = CarManager()
scoreboard = Scoreboard()

# Set up key press listeners
listen_key()

# Main game loop
is_game_on = True
while is_game_on:
    time.sleep(cars.cars_speed)  # Pause for a short time, making cars move slower at the start
    cars.create_car()  # Create a new car at random intervals
    cars.move_cars()  # Move all cars on the screen
    screen.update()  # Update the screen with the latest movements

    # Check if the player collides with any car
    if cars.turtle_collision_with_car(player):
        is_game_on = False  # End the game if there's a collision
        scoreboard.game_over()  # Display the game over message

    # Check if the player has reached the finish line
    if player.is_at_finish_line():
        scoreboard.increase_lvl()  # Increase the level if the player finishes
        player.go_to_start()  # Reset player to starting position
        cars.cars_speed *= 0.9  # Increase car speed for the next level

# Close the game window on click
screen.exitonclick()