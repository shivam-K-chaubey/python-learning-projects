import turtle as t
import random

colors = ["red", "blue", "yellow", "green", "orange", "purple"]
screen = t.Screen()

choice = screen.textinput(
    title="Make your bet",
    prompt="Enter a turtle color: "
)
screen.setup(600, 500)

turtles = []

def create_turtles():
    for color in colors:
        tim = t.Turtle(shape="turtle")
        tim.color(color)
        tim.penup()
        turtles.append(tim)

def set_position():
    y = 100
    for turtle in turtles:
        turtle.goto(-250, y)
        y -= 40
def finish_line():
    line = t.Turtle()
    line.hideturtle()
    line.teleport(250, 130)
    line.setheading(270)
    line.forward(250)

create_turtles()
set_position()
finish_line()
winner = ""
race_is_on = True
while race_is_on:
    for turtle in turtles:
        turtle.forward(random.randint(1, 5))
        if turtle.xcor() >= 250:
            winner = turtle.pencolor()
            race_is_on = False
            break

hand = t.Turtle()
if choice == winner:
    hand.hideturtle()
    hand.write(f"Congratulation! {choice.title()} Won", align="center")
else:
    hand.hideturtle()
    hand.write(f"{winner.title()} Won, You Lose", align="center")
print(winner)
screen.mainloop()