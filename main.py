from turtle import Screen
from walking_turtle import Walking_turtle
from food import Food
import time

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.listen()

food = Food()
turtle = Walking_turtle()

screen.onkey(turtle.move_forward, "w")
screen.onkey(turtle.move_backward, "s")
screen.onkey(turtle.move_left, "a")
screen.onkey(turtle.move_right, "d")

while True:
    screen.update()
    time.sleep(0.1)

    # When turtle eats the food, the food must be revived elsewhere on the screen.
    if turtle.distance(food) <= 15:
        food.spawn()
    # When turtle go outside the screen it should be placed back on the center of the screen.
    if turtle.xcor() > 290 or turtle.xcor() < -290 or turtle.ycor() > 290 or turtle.ycor() < -290:
        turtle.go_back()
