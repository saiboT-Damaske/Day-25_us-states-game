import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States quiz game")
image = "./blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


def get_mouse_click_coor(x, y):
    print(x, y)


data = pd.read_csv("50_states.csv")
correct_states = 0
game_is_on = True

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
correctly_guessed_states = []
while game_is_on:
    guess = screen.textinput(title=f"Guess a state ({correct_states}/50)", prompt="name:").title()
    turtle.onscreenclick(get_mouse_click_coor)

    if guess == "Exit":
        missing_states = [state for state in data.state if state not in correctly_guessed_states]
        # for state in data.state:
        #     if state not in correctly_guessed_states:
        #         missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        game_is_on = False

    for stat in data.state:
        if guess == stat and guess not in correctly_guessed_states:
            correct_states += 1
            x_cor = data[data["state"] == guess].x.iloc[0]
            y_cor = data[data["state"] == guess].y.iloc[0]
            writer.goto(x_cor, y_cor)
            writer.write(f"{guess}", align="center", font=("arial", 8, "normal"))
            correctly_guessed_states.append(guess)

    if correct_states == 50:
        writer.goto(0, 0)
        writer.write(f"Congratulations! You guessed all 50 states", align="center", font=("arial", 20, "normal"))
        game_is_on = False


turtle.mainloop()
