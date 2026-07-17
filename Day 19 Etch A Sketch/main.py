import turtle

screen = turtle.Screen()
screen.setup(600, 500)

tim = turtle.Turtle()
def move_upwards():
    tim.setheading(90)
    tim.forward(25)
def move_downwards():
    tim.setheading(270)
    tim.forward(25)

def move_left():
    tim.setheading(180)
    tim.forward(25)

def move_right():
    tim.setheading(0)
    tim.forward(25)
def erase():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.onkey(move_upwards, "Up")
screen.onkey(move_downwards, "Down")
screen.onkey(move_right, "Right")
screen.onkey(move_left, "Left")
screen.onkey(erase, "c")
screen.listen()
screen.mainloop()