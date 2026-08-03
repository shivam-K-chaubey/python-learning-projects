from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-17, 0), (-34, 0)]
MOVE_DISTANCE = 17

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        for position in STARTING_POSITIONS:
            self.create_segment(position)
        self.head = self.segments[0]

    def create_segment(self, position):
        tim = Turtle()
        tim.shape("square")
        tim.penup()
        tim.shapesize(stretch_wid=0.8, stretch_len=0.8)
        tim.color("white")
        tim.goto(position)
        self.segments.append(tim)

    def move(self):
        """Move the snake one step forward."""
        for seg in range(len(self.segments) - 1, 0 , -1):
            new_position = self.segments[seg - 1].position()
            self.segments[seg].goto(new_position)

        self.head.forward(MOVE_DISTANCE)

    def extend(self):
        last_seg_pos = self.segments[-1].position()
        self.create_segment(last_seg_pos)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
