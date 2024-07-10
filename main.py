import random
import turtle

# Presets
draw = turtle.Turtle()
screen = turtle.Screen()
screen.colormode(255)
angle = 0


def get_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


while angle < 360:
    draw.color(get_color())
    draw.speed(0)
    draw.circle(100)
    angle += 10
    draw.setheading(angle)

screen.exitonclick()