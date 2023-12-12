# USA States Quiz Game v0.1

import turtle
import pandas

# Set up the turtle screen
screen = turtle.Screen()
screen.title("U.S.A. States Quiz")

# Load and display the blank U.S. states map
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Load the U.S. states data from the CSV file
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

# Main game loop
while len(guessed_states) < 50:
    # Get user input for the state name
    answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's the State's Name?").title()

    # Check if the user wants to exit the game
    if answer == "Exit":
        # Find the states that were not guessed
        missed_states = [state for state in all_states if state not in guessed_states]
        # Create a DataFrame with missed states and save it to a new CSV file
        missed_states_df = pandas.DataFrame(missed_states, columns=["Missed States"])
        missed_states_df.to_csv("missed_states.csv", index=False)
        break
    
    # Check if the user's guess is a valid U.S. state
    if answer in all_states:
        guessed_states.append(answer)
        
        # Create a turtle to display the correctly guessed state on the map
        turtle_pen = turtle.Turtle()
        turtle_pen.hideturtle()
        turtle_pen.penup()
        
        # Get the coordinates of the guessed state and display the state name
        state_data = data[data.state == answer]
        turtle_pen.goto(int(state_data.x), int(state_data.y))
        turtle_pen.write(answer)

# End of the game
print("Quiz Ended\n")
# END OF CODE
