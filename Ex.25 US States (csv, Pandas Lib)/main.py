import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guess_states = []

while len(guess_states) < 50:
    answer_state = screen.textinput(title=f"{len(guess_states)}/50 States Correct", prompt="What's another State's name?").title()

    if answer_state == "Exit":
        # missing_states = []
        # for state in all_states:
        #     if state not in guess_states:
        #         missing_states.append(state)
        missing_states = [state for state in all_states if state not in guess_states] # Same as previous 4 lines
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    #If answer_state is one of the states in all the states of the 50_states.csv:
    #   If they got it right:
    #       Create a turtle to write the name of the state at the state's x and y coordinates
    if answer_state in all_states:
        guess_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)


# # Getting x and y positions by clicking a mouse
# def get_mouse_click_coordinates(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coordinates)
# turtle.mainloop() # This is an alternative to screen.exitonclick(), but it enable us to click on the screen.

