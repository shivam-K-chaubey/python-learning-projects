import turtle

screen = turtle.Screen()
screen.setup(600, 500)

tim = turtle.Turtle()

def move_forwards():
    #Move tim forwards by 5 units
    tim.forward(10)

def move_backwards():
    #Move tim backwards by 5 unit
    tim.backward(10)

def turn_left():
    new_angle = tim.heading() + 10
    tim.setheading(new_angle)

def turn_right():
    new_angle = tim.heading() - 10
    tim.setheading(new_angle)

def erase():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.onkey(move_forwards, "space")
screen.onkey(move_backwards, "b")
screen.onkey(turn_right, "Down")
screen.onkey(turn_left, "Up")
screen.onkey(erase, "c")
screen.listen()
screen.mainloop()