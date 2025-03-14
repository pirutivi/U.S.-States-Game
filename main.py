import turtle
import pandas

screen=turtle.Screen()

screen.title("U.S. States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data=pandas.read_csv("50_states.csv")
all_state_list=data["state"].to_list()

guessed_state=[]
while len(guessed_state)<50:
        answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct", prompt="What's another states name?.").title()
        print(answer_state)
        if answer_state=="Exit":
                missing_states=[state for state in all_state_list if state not in guessed_state]
                #missing_states=[]
                #for state in all_state_list:
                #        if state not in guessed_state:
                #                missing_states.append(state)
                new_data=pandas.DataFrame(missing_states)
                new_data.to_csv("missing_state.csv")

                break
        if answer_state in all_state_list:
                guessed_state.append(answer_state)
                tom=turtle.Turtle()
                tom.hideturtle()
                tom.penup()
                tom.color("green")
                state_data=data[data.state==answer_state]
                tom.goto(int(state_data.x),int(state_data.y))
                tom.write(answer_state)




