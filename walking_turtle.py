from turtle import Turtle


class Walking_turtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("orange", "green")

    def go_back(self):
        self.goto(0, 0)

# Make commands to move the turtle.
    def move_forward(self):
        self.forward(20)

    def move_backward(self):
        self.backward(20)

    def move_left(self):
        self.left(15)

    def move_right(self):
        self.right(15)
