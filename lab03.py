# lab03.py for Ryan Stuart
# CS20, Spring 2016, Instructor: Phill Conrad
# Draw some initials using turtle graphics

import turtle
import math

def drawR(turtle, height, width):
    """
    draw the letter R using turtle, with some height and width
    """
    # Face upward and put pen down
    turtle.setheading(90)
    turtle.pendown()
    # Go forward and turn right
    turtle.forward(height)
    turtle.right(90)
    # Draw loop of R
    turtle.forward((2.0/3.0)*width)
    turtle.right((180.0/math.pi)*math.atan((3.0/4.0)*height/width))
    turtle.forward(math.sqrt(((1.0/4.0)*height)**2+((1.0/3.0)*width)**2))
    turtle.right(180.0-(360.0/math.pi)*math.atan((3.0/4.0)*height/width))
    turtle.forward(math.sqrt(((1.0/4.0)*height)**2+((1.0/3.0)*width)**2))
    turtle.right((180.0/math.pi)*math.atan((3.0/4.0)*height/width))
    turtle.forward((2.0/3.0)*width)
    # Draw last leg
    turtle.left(90.0+((180.0/math.pi)*math.atan((2.0)*width/height)))
    turtle.forward(math.sqrt(((1.0/2.0)*height)**2+width**2))
    # Pick up pen
    turtle.penup()

def drawS(turtle, height, width):
    """
    draw the letter S using turtle, with some height and width
    """
    # Pick pen up and move a little to the right
    turtle.penup()
    turtle.setheading(0)
    turtle.forward((1.0/6.0)*width)
    # Put pen down and draw bottom of S
    turtle.pendown()
    turtle.forward((2.0/3.0)*width)
    # Draw first curve
    turtle.left((180.0/math.pi)*math.atan((3.0/2.0)*height/width))
    turtle.forward(math.sqrt(((1.0/6.0)*width)**2+((1.0/4.0)*height)**2))
    turtle.left(180.0-(360.0/math.pi)*math.atan((3.0/2.0)*height/width))
    turtle.forward(math.sqrt(((1.0/6.0)*width)**2+((1.0/4.0)*height)**2))
    turtle.left((180.0/math.pi)*math.atan((3.0/2.0)*height/width))
    # Draw middle of S
    turtle.forward((2.0/3.0)*width)
    # Draw second curve
    turtle.right((180.0/math.pi)*math.atan((3.0/2.0)*height/width))
    turtle.forward(math.sqrt(((1.0/6.0)*width)**2+((1.0/4.0)*height)**2))
    turtle.right(180.0-(360.0/math.pi)*math.atan((3.0/2.0)*height/width))
    turtle.forward(math.sqrt(((1.0/6.0)*width)**2+((1.0/4.0)*height)**2))
    turtle.right((180.0/math.pi)*math.atan((3.0/2.0)*height/width))
    # Draw top of S, pick up pen, and move a little to the right
    turtle.forward((2.0/3.0)*width)
    turtle.penup()
    turtle.forward((1.0/6.0)*width)

def drawRS(turtle, letterWidth, letterHeight, spacing):
    """
    draw the initials R and S using turtle, with some letterWidth, letterHeight,
    and spacing
    """
    # Draw R
    drawR(turtle, letterHeight, letterWidth)
    # Draw Spacing
    turtle.setheading(0)
    turtle.forward(spacing*letterWidth)
    # Draw S
    drawS(turtle, letterHeight, letterWidth)


fred = turtle.Turtle()

def go():
    # Pickup pen and go to first starting point
    fred.penup()
    fred.goto(-200,200)
    # Draw first set of initials
    fred.pendown
    drawRS(fred, 40, 40, 2)
    # Go to second starting point
    fred.goto(100,50)
    # Draw second set of initials
    drawRS(fred, 50, 200, 0.5)
    # Go to third starting point
    fred.goto(-255,-255)
    # Draw third set of initials
    drawRS(fred, 150, 290, 1)
    
