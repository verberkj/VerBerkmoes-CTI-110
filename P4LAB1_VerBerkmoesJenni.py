# Jenni VerBerkmoes
# 10/19/2026
# P4LAB1
# Use turtle and loops to draw a square and a triangle

# Import the library
import turtle

# Create the turtle window and drawing object
win = turtle.Screen()
pen = turtle.Turtle()
win.bgcolor("pink")

# Set turtle options
pen.pensize(5)
pen.pencolor("darkgreen")
pen.shape("arrow")

# Fill triangle with color
pen.fillcolor("black")
pen.begin_fill()

# For loop to draw the triangle that executes 3 times
for lines in range(3):
    pen.forward(100)
    pen.left(120)

# Fill triangle with color
pen.end_fill()

# While loop to draw the square, that executes 4 times
lines = 4
while lines > 0:
    pen.forward(100)
    pen.right(90)
               
    lines = lines - 1

win.mainloop()
