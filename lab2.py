# Contributer Name(s): Asa Henry, Kai Gelbard
# Email(s): ajh728@nau.edu, krg349@nau.edu

# Submission Confirmation Number: 8d80551f-29bf-435d-9a13-94c5744056c6

#Imports
import random
import math
import turtle


#Main
def main():
    drew = turtle.Turtle()
    drew.speed('fastest')

    num_Needles = 1000

    print(f"PI = {showBuffonsNeedlesPi(drew, num_Needles)}")


#Functions
def showMontePi(numDarts):
    wn = turtle.Screen()
    drawingT = turtle.Turtle()

    wn.setworldcoordinates(-2, -2, 2, 2)

    drawingT.goto(-1, 0)
    drawingT.down()
    drawingT.goto(1, 0)

    drawingT.up()
    drawingT.goto(0, 1)
    drawingT.down()
    drawingT.goto(0, -1)

    inCircle = 0
    drawingT.up()
    
    for i in range(numDarts):
        x = random.random()
        y = random.random()

        distance = math.sqrt(x**2 + y**2)

        drawingT.goto(x, y)

        if distance <= 1:
            inCircle = inCircle + 1
            drawingT.color("blue")
        else:
            drawingT.color("red")

        drawingT.dot()

    pi = inCircle / numDarts * 4
    wn.exitonclick()

    return pi    


def showBuffonsNeedlesPi(drew, num_Needles):
    
    # Window setup
    wn = turtle.Screen()
    wn.setworldcoordinates(-1, -1, 1, 1)

    # Simulation var(s)
    dist_btwx_parallel_lines = 1
    num_Hits = 0

    # Simulation setup
    drawParallelLines(drew, dist_btwx_parallel_lines / 2)

    # Needle setup
    needle_len = dist_btwx_parallel_lines


    for _ in range(num_Needles):
        x = random.uniform(-1, 1)
        y = random.uniform(-0.5, 0.5)
        theta = random.uniform(0, 180)

        num_Hits = drawCurrentNeedle(drew, x, y, needle_len, theta, num_Hits)


    pi = (2 * num_Needles) / (num_Hits)

    return pi


def resetSeth(drew):
    drew.seth(0)


def drawParallelLines(drew, dist):
    drew.penup()
    drew.goto(-1, -dist)

    drew.pendown()
    drew.forward(1.98)

    drew.penup()
    drew.goto(-1, dist)

    drew.pendown()
    drew.forward(1.98)

    drew.penup()


def drawCurrentNeedle(drew, x, y, needle_len, theta, num_Hits):
    return collisionCheck(drew, x, y, needle_len, theta, num_Hits)


def collisionCheck(drew, x, y, needle_len, theta, num_Hits):
    hits = num_Hits
    

    drew.goto(x, y)
    drew.seth(theta)
    drew.forward(needle_len / 2) # Moves the turtle to the x and y at the end of the upper half of the needle

    if drew.ycor() > 0.5:
        hits = num_Hits + 1
        drew.color("green")

        drew.pendown()
        drew.forward(-needle_len)
        drew.penup()

        return hits


    drew.goto(x, y)
    drew.forward(-(needle_len / 2)) # Moves the turtle to the x and y at the end of the lower half of the needle

    if drew.ycor() < -0.5:
        hits = num_Hits + 1
        drew.color("green")
        drew.pendown()
        drew.forward(needle_len)
        drew.penup()
  
        return hits
    else:
        drew.color("red")

        drew.goto(x, y)
        drew.seth(theta)
        drew.pendown()
        drew.forward(needle_len / 2)
        drew.penup()
        resetSeth(drew)

        drew.goto(x, y)
        drew.seth(theta - 180)
        drew.pendown()
        drew.forward((needle_len / 2))
        drew.penup()
        resetSeth(drew)
    
    return hits


main()


turtle.Screen().exitonclick()