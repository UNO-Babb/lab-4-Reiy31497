#TurtleGraphics.py
#Name:Reiy Beaudoin
#Date:9/22/24
#Assignment:Lab 4

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)
        
def drawPolygon(Sam, sides):
    for s in range(sides):
        Sam.forward(50)
        Sam.right(360/sides)
        
def fillCorner(Sam, corner):
    drawSquare(Sam, 100)
    Sam.begin_fill()
    drawSquare(Sam, 50)
    Sam.end_fill()
    
def squaresInSquares(Sam, num):
    drawSquare(Sam, 20)
    Sam.penup()
    Sam.goto(-10, -30)
    Sam.left(90)
    Sam.pendown()
    drawSquare(Sam, 40)
    Sam.penup()
    Sam.goto(40, -40)
    Sam.left(90)
    Sam.pendown()
    drawSquare(Sam, 60)
    Sam.penup()
    Sam.goto(50, 30)
    Sam.left(90)
    Sam.pendown()
    drawSquare(Sam, 80)
    Sam.penup()
    Sam.goto(-40, 40)
    Sam.left(90)
    Sam.pendown()
    drawSquare(Sam, 100)


def main():
    myTurtle = turtle.Turtle()
    #drawPolygon(myTurtle, 5) #draws a pentagon
    #drawPolygon(myTurtle, 8) #draws an octogon
    #drawPolygon(myTurtle, 12) 

    #drawSquare(myTurtle, 100)

    fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    #squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
