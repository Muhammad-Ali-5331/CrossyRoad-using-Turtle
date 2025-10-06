from turtle import Turtle

# Define constants for the player's starting position, movement distance, and the finish line's Y-coordinate
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

# Create a Player class that inherits from the Turtle class
class Player(Turtle):
    def __init__(self):
        super().__init__()  # Initialize the Turtle superclass
        self.shape("turtle")  # Set the player's shape to a turtle
        self.penup()  # Lift the pen to avoid drawing lines when moving
        self.color("white")  # Set the player's color to white
        self.setheading(90)  # Set the player's direction to face upwards
        self.go_to_start()  # Place the player at the starting position


    # Method to move the player up by a fixed distance
    def move_up(self):
        self.forward(MOVE_DISTANCE)

    # Method to reset the player to the starting position
    def go_to_start(self):
        self.goto(STARTING_POSITION)

    # Method to check if the player has reached the finish line
    def is_at_finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:  # Check if the player's Y-coordinate is at or above the finish line
            return True  # Return True if the player has reached the finish line