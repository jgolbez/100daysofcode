import turtle
import pandas

states_image = "blank_states_img.gif"
screen = turtle.Screen()
screen.title("US States Game")

screen.addshape(states_image)
turtle.shape(states_image)
turtle.tracer(0)

number_correct = 0
states_data = pandas.read_csv("50_states.csv")
print(states_data)
state_list = states_data["state"].to_list()

game_running = True
while number_correct < 50 and game_running:
    answer_state = screen.textinput(title=f"Guess the State [{number_correct}/50]", prompt="Type the name of a State").title()
    print(answer_state)
    if answer_state in state_list:
        number_correct += 1
        answer = states_data[states_data.state == f"{answer_state}"]
        turtle.goto(int(answer.x), int(answer.y))
        turtle.write(f"{answer_state}")
        state_list.remove(answer_state)
    elif answer_state == "Exit":
        game_running = False
        missed_states_dict = {"Missed States": state_list}
        df = pandas.DataFrame(missed_states_dict)
        df.to_csv("missed_states.csv")




#screen.exitonclick()
