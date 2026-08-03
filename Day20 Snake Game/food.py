import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("green")

    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 250)
        self.goto(x, y)

