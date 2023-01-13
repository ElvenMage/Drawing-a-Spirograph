import random
import turtle as t
from turtle import Screen

timmy = t.Turtle()

# Defining the colors as rgb
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour

# Speed of the turtle
timmy.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        #you can adjust the radius of the circle
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)
        timmy.circle(100)

#You can adjust the gap as you wish
draw_spirograph(15)


screen = Screen()
screen.exitonclick()
