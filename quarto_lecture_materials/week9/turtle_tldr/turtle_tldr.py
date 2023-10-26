

import turtle

# # Create a turtle object named pet
# pen = turtle.Turtle()

# # Set the turtle's speed to the fastest
# pen.speed(0)

# # Use forward and left to draw a triangle.
# # stamp at each vertex
# for i in range(3):  # Will create 36 stamped arrows, each at a different angle
#     pen.forward(50)  # Move pen forward by 10 units
#     pen.stamp()  # Stamp the arrow shape onto the canvas
#     pen.left(120)  # Turn pen around to head back to the origin

# # Re-position pen for the next part of the drawing
# # specifically, go to coordinate 100, -100
# pen.penup()  # Lift the pen so pen doesn't draw while moving
# pen.goto(100, -100)  # Move pen to a new position
# pen.pendown()  # Put the pen down so pen is ready to draw again

# # Change pen's color to blue and draw a square
# pen.color("blue")
# for _ in range(4):
#     pen.forward(100)
#     pen.right(90)

# # now go to coordinate -100, 100
# pen.penup()  # Lift the pen
# pen.goto(-100, 100)  # Move pen to a new position
# pen.pendown()  # Put the pen

# # Change the color mode to allow RGB color values
# turtle.colormode(255)

# # Set a new color using an RGB tuple and draw another square
# mycolor = (255, 0, 120)
# pen.color(mycolor)
# for _ in range(4):
#     pen.forward(100)
#     pen.right(90)

# # Hide the turtle and display the result
# pen.hideturtle()
# turtle.done()
