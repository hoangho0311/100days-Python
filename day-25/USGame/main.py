import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S")

image= "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

def get_mouse(x,y):
    print(x,y)

with open("50_states.csv") as data_file:
    data = pandas.read_csv(data_file)
    all_state = data.state.to_list()
guess=[]
while len(guess)<50:
    answer = screen.textinput("Guess","What is another")
    if answer == "Exit":
        missing_state =[]
        for state in all_state:
            if state not in guess:
                missing_state.append(state)
        file = pandas.DataFrame(missing_state)
        file.to_csv("missing.csv")
        break
    if answer in all_state:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        dataXY = data[data.state == answer]
        t.goto(int(dataXY.x), int(dataXY.y))
        t.write(answer)
        guess.append(answer)


