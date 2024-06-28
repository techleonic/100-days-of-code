import  turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

def get_mouse_cor (x, y):
    print(x, y)

#Pandas data frame
df = pandas.read_csv("50_states.csv")
states = df.state.to_list()
print(states)

#turtle write state
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

#score
total = len(states)
guessed_states = []
is_game_on =  True

#states to learn
learn_state = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{total} Guess the State", prompt="What's another state's name?")
    answer_state =  answer_state.title()

    if answer_state == "Exit":
        for state in states:
            if state not in guessed_states:
                learn_state.append(state)
        new_df =  pandas.DataFrame(learn_state)
        new_df.to_csv("states_to_learn.csv")
        break

    if answer_state in states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        row = df[df.state == answer_state]
        print(row)
        writer.goto(int(row.x.iloc[0]), int(row.y.iloc[0]))
        writer.write(f"{row.state.item()}")



# turtle.mainloop()
# turtle.onscreenclick(get_mouse_cor)
