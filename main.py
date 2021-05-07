import pandas
from turtle import Screen, Turtle

screen = Screen()
screen.title("India State Game")
screen.setup(width=583, height=684)
screen.bgpic("india_map.gif")

DATA = pandas.read_csv("india_state.csv")
STATES = DATA["state"].to_list()
correct_guess = 0
no_of_guess = 0
guessed_states = []
missed_states = []

while correct_guess < len(STATES):
    answer_state = screen.textinput(title=f"{correct_guess}/{len(STATES)} | {no_of_guess} Attempts",
                                    prompt="whats another state name ? \nType 'exit' to end").title()
    no_of_guess += 1
    if answer_state == "Exit":
        for state in STATES:
            if state not in guessed_states:
                missed_states.append(state)
        missed_data = pandas.DataFrame(missed_states)
        missed_data.to_csv("states_to_learn.csv", index=False, header=["state"])
        break
    if answer_state in STATES:
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)
            map_state = Turtle()
            map_state.penup()
            state_data = DATA[DATA.state == answer_state]
            map_state.goto(int(state_data.x), int(state_data.y))
            map_state.hideturtle()
            map_state.write(arg=answer_state)
            correct_guess += 1
