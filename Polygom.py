import turtle  # importing library
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300, 400)
polygon = turtle.Turtle()  # defined variable

num_sides = 6  # variable
side_length = 70
angle = 360.0 / num_sides
# iterate loop for total number of sides
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()

import turtle

turtle.Screen().bgcolor("Aqua")
board = turtle.Turtle()

# first triangle for star
board.forward(100)  # draw base

board.left(120)
board.forward(100)

board.left(120)
board.forward(100)

board.penup()
board.right(150)
board.forward(50)

# second triangle for star
board.pendown()
board.right(90)
board.forward(100)

board.right(120)
board.forward(100)
