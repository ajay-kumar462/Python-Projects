import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

game_on = True
score = 0
guessed_states = []
data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()

while len(guessed_states) < 50:
    answer_state = screen.textinput(f"{len(guessed_states)}/50 Guessed Correct", prompt="Name another state").title()
    if answer_state == "Exit":
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")

        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        all_states.remove(answer_state)
        state_data = data[data["state"] == answer_state]
        label = turtle.Turtle()
        label.penup()
        label.hideturtle()
        label.goto(state_data["x"].values[0], state_data["y"].values[0])
        label.write(f"{answer_state}", align="center")
        with open("states_list.txt", mode="a") as main:
            main.write(answer_state + "\n")
            score += 1
    # states_to_learn.csv

turtle.mainloop()