import turtle as t
import random

def draw_random_lines(num_lines):
    for _ in range(num_lines):
        t.color(random.random(), random.random(), random.random())
        t.penup()
        t.goto(random.randint(-200, 200), random.randint(-200, 200))
        t.pendown()
        t.setheading(random.randint(0, 360))
        t.forward(random.randint(50, 200))

def draw_random_circles(num_circles):
    for _ in range(num_circles):
        t.color(random.random(), random.random(), random.random())
        t.penup()
        t.goto(random.randint(-200, 200), random.randint(-200, 200))
        t.pendown()
        t.circle(random.randint(10, 100))

def main():
    t.speed(0)
    draw_random_lines(50)
    draw_random_circles(30)
    t.hideturtle()
    t.done()

main()


