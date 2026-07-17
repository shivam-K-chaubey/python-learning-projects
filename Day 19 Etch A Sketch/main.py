import turtle

screen = turtle.Screen()
screen.setup(600, 500)

tim = turtle.Turtle()
def up_m():
    tim.setheading(90)
    tim.forward(25)
def down_m():
    tim.setheading(270)
    tim.forward(25)

def left_m():
    tim.setheading(180)
    tim.forward(25)

def right_m():
    tim.setheading(0)
    tim.forward(25)
def erase():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.onkey(up_m, "Up")
screen.onkey(down_m, "Down")
screen.onkey(right_m, "Right")
screen.onkey(left_m, "Left")
screen.onkey(erase, "c")
screen.listen()
screen.mainloop()