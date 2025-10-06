from turtle import Turtle

# Define the font style for displaying text
FONT = ("Arial", 15, "normal")

# Create a Scoreboard class that inherits from the Turtle class
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()  # Initialize the Turtle superclass
        self.hideturtle()  # Hide the turtle cursor
        self.penup()  # Lift the pen to avoid drawing lines when moving
        self.color("white")  # Set the text color to white
        self.lvl = 1  # Initialize the level to 1
        self.goto(-240, 260)  # Position the scoreboard at the top left of the screen
        self.display_lvl()  # Display the initial level on the screen

    # Method to display the current level on the screen
    def display_lvl(self):
        self.write(f"Level = {self.lvl}", align="center", font=FONT)

    # Method to increase the level and update the display
    def increase_lvl(self):
        self.lvl += 1  # Increment the level by 1
        self.clear()  # Clear the previous level display
        self.display_lvl()  # Display the new level

    # Method to display "GAME OVER" at the center of the screen
    def game_over(self):
        self.home()  # Move the turtle to the center of the screen
        self.write("GAME OVER", align="center", font=FONT)