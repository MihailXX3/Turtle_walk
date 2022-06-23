from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.shapesize(0.5, 0.5)
        self.shape("circle")
        self.penup()
        self.color("purple", "pink")
        self.spawn()

# Make command to respawn the food elsewhere on the screen.
    def spawn(self):
        random_y = random.randint(-280, 280)
        random_x = random.randint(-280, 280)
        self.goto(x=random_x, y=random_y)
