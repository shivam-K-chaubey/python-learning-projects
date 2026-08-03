from turtle import Turtle

SCORE_POSITION = (0, 255)
SCORE_FONT = ("Comic Sans MS", 16, "normal")
GAME_OVER_FONT = ("Comic Sans MS", 24, "bold")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(SCORE_POSITION)
        self.score = 0
    def display_score(self):
        self.write(f"Score: {self.score}", font=SCORE_FONT, align="center")
    def increase_score(self):
        self.score += 1
        self.clear()
        self.display_score()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over", font=GAME_OVER_FONT, align="center")


