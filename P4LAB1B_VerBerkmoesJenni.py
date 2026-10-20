# Jenni VerBerkmoes
# 10/20/2026
# P4LAB1b - Inititials
# Use turle to write a program that displays my first and last initials

# Import turtle

import turtle

# Create the turtle window and drawing object

win = turtle.Screen()
jen = turtle.Turtle()
win.bgcolor("magenta")

# Set turtle options
jen.pensize(50)
jen.pencolor("black")
jen.shape("arrow")

# Move starting point of pen
jen.penup()
jen.left(200)
jen.forward(100)
jen.pendown()

# Draw first initial "J"
jen.setheading(270)
jen.forward(200)
jen.circle(-50, 180)  

# Move pen to starting point for last initial
jen.penup()
jen.forward(200)
jen.right(90)
jen.forward(200)
jen.pendown()

# Draw last initial "V"
jen.right(60)
jen.forward(270)
jen.left(120)
jen.forward(270)


win.mainloop()