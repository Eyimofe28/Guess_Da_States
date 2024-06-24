import turtle
import pandas

# Setting up the screen.
screen = turtle.Screen()
screen.setup(height=540, width=770)
screen.title("Guess Da States!")

image = "blank_states_img.gif"
screen.addshape(image)  # This adds the image as a shape option in turtle
turtle.shape(image)  # Adds the image to the screen.

write = turtle.Turtle()
write.speed(0)
write.hideturtle()
write.penup()
write.goto(160, 245)
write.write("Enter 'Exit' to leave the game.", font=("Times New Roman", 12, "bold"))

count = 0
correct_guesses = []

# Reading the United States data using Pandas.
the_states_data = pandas.read_csv("50_states.csv")
the_states = the_states_data["state"].to_list()

while count < 50:
    state_guess = turtle.textinput(title=f"{count}/50 States Correct", prompt="Enter a state in the US: ").title()

    if state_guess == "Exit":
        states_to_learn_list = []
        for i in the_states:
            if i not in correct_guesses:
                states_to_learn_list.append(i)

        states_to_learn_dict = {
            "States To Learn": states_to_learn_list
        }

        newData = pandas.DataFrame(states_to_learn_dict)
        newData.to_csv('states_to_learn.csv')
        break

    if state_guess in the_states and state_guess not in correct_guesses:
        count += 1
        correct_guesses.append(state_guess)

        state_row = the_states_data[the_states_data.state == state_guess]
        x_coord = int(state_row.x.item())  # I was struggling with an error but this item() method cleared it out.
        y_coord = int(state_row.y.item())  # the item method fetches the actual raw data {i.e, data without index}.

        write = turtle.Turtle()
        write.hideturtle()
        write.penup()
        write.goto(x_coord, y_coord)
        write.write(state_guess, font=("Times New Roman", 10, "italic"))


# def get_click_coord(x, y):
#     print(x, y)
#
#
# # Calling the function as an object since we would get the x & y coord by clicking the screen.
# turtle.onscreenclick(get_click_coord)
# turtle.mainloop()  # Alternative way to keep the screen on.

screen.exitonclick()
