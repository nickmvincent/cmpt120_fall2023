import turtle as t
import random
import math

def draw_square(side_length):
    for _ in range(4):
        t.forward(side_length)
        t.right(90)

def main():
    t.speed(0)
    for i in range(360):  # iterating through 360 degrees to cover a full sine wave cycle
        t.penup()
        x = i - 180  # shifting i by 180 to have x range from -180 to 180
        y = math.sin(math.radians(x)) * 100  # scaling the sine wave
        t.goto(x*2, y)  # stretching the x-coordinates to spread out the pattern
        t.pendown()
        t.color(random.random(), random.random(), random.random())
        side_length = abs(math.sin(math.radians(x)) * 50) + 10  # varying square size based on sine value
        draw_square(side_length)
    t.hideturtle()
    t.done()

main()
