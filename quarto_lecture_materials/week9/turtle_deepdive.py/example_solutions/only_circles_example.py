import turtle as t
import random

def draw_random_circle():
    t.penup()
    t.goto(random.randint(-300, 300), random.randint(-300, 300))
    t.pendown()
    t.color(random.random(), random.random(), random.random())
    t.begin_fill()
    t.circle(random.randint(10, 100))
    t.end_fill()

def main():
    t.speed(0)
    for _ in range(50):
        draw_random_circle()
    t.hideturtle()
    t.done()

main()
