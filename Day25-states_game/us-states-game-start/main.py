import turtle
import pandas
from pen import Pen

#* set up the screen
screen = turtle.Screen()
screen.title("U.S States Game")
screen.setup(height=500, width=730)
image = "Day25-states_game/us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game_is_on = True
states = pandas.read_csv("Day25-states_game/us-states-game-start/50_states.csv")
states_list = states.state.to_list()
guessed_states = []
while game_is_on:

    count = len(guessed_states)

    #* asks the user for input
    if count == 0:
        answer = turtle.textinput("Guess a state", "type a state's name").title()
    elif count == 50:
        game_is_on = False
        break
    else:
        answer = turtle.textinput(f"Guese a state {count}/50", "type another state's name").title()

    #* checks the answer
    if answer in states_list and answer not in guessed_states:

        #* adds it to guessed states list
        guessed_states.append(answer)

        #* query the coordinate of the correct state
        coordinates = states[states["state"] == answer]
        x = int(coordinates['x'])
        y = int(coordinates['y'])

        #* write the namw of the state in the right coordinate
        Pen(answer, x, y)
    
    else:
        continue


screen.exitonclick()

