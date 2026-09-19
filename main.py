import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")

image = 'blank_states_img.gif'
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states)  < len(all_states):
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state name?")

    answer_state = answer_state.title()

    if answer_state is None:
        break

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x.item()), int(state_data.y.item()))
        t.write(answer_state)

screen.exitonclick()