 # Name: Asa Henry
 # Email: ajh728@nau.edu

# Imports
import turtle

# Main
def main():
    # Turtle declaration
    drew = turtle.Turtle()

    Exercise_One_Two(drew)
    Exercise_One_Three(drew)
    Exercise_One_One(drew)
    Exercise_One_Four(drew)
    Exercise_One_Five(drew)

# Global Functions (Functions used in multiple exercises)
def Turtle_Reset(turtle, x, y):
    turtle.goto(x, y)
    turtle.seth(0)
    turtle.pendown()


# Exercise 1.2 : Draw a 5 pointed star
def Exercise_One_Two(turtle):
    
    # Sets up the turtle for this exercise
    turtle.penup()
    turtle.goto(150, 250)
    
    # Functions for this exercise
    def DrawPeak(t, point_angle, side_length):
        t.forward(side_length)
        t.right(point_angle)

    def DrawPentangle(t):
        t.pendown()
        for _ in range(5):
            DrawPeak(t, point_angle, side_length)


    # Star angles var(s) for star
    point_angle = 144

    # Star side lengths var(s) for star
    side_length = 100

    # Turtle Setup, for this exercise
    turtle.seth(70)

    DrawPentangle(turtle)

    turtle.penup()


# Exercise 1.3 : Draw a star with n points
def Exercise_One_Three(turtle):

    # Sets up the turtle for this exercise
    Turtle_Reset(turtle, -250, 250)

    # Functions
    def DrawValley(t, points, side_length):
        for _ in range(2):
            t.forward(side_length)
            t.right(180 - (180 / points))

    def DrawNangle(t, points): # Nangle being derived from another name for stars (i.e. 5 pointed star: Pentangle)
        for _ in range(points):
            DrawValley(t, points, side_length)
            t.left(360 / points)

    # Triangle var(s)
    side_length = 100

    # Nangle var(s)
    points = 19

    DrawNangle(turtle, points)

    turtle.penup()


# Exercise 1.1 : Draw a flower using n squares
def Exercise_One_One(turtle):
    
    #Sets up the turtle
    Turtle_Reset(turtle, -150, -250)

    # Functions for this exercise
    def DrawSquare(turtle, side_length):
        for _ in range(4):
            turtle.forward(side_length)
            turtle.right(90)

    def DrawFlower(turtle, amt_sqrs):
        for _ in range(amt_sqrs):
            DrawSquare(turtle, sqr_side_length)
            turtle.right(360 / amt_sqrs)

    # Function var(s)
    amt_sqrs = 5

    # Square side length var(s)
    sqr_side_length = 100

    #DrawSquare(star_turtle, sqr_side_length)
    DrawFlower(turtle, amt_sqrs)

    turtle.penup()

# Exercise 1.4 : Free draw
def Exercise_One_Four(turtle):

    Turtle_Reset(turtle, 150, -250)

    # Functions
    def DrawY(t):
        t.forward(stem_length)

        x = t.xcor()
        y = t.ycor()

        t.left(split_angle)
        t.forward(split_length)
        t.right(split_angle)

        t.penup()
        t.goto(x, y)
        t.pendown()

        t.right(split_angle)
        t.forward(split_length)
        t.left(split_angle)

    def Draw_Snow_Flake(t):
        wings = 7

        x = t.xcor()
        y = t.ycor()

        for _ in range(wings):
            DrawY(t)
            t.goto(x, y)
            t.left(360 / wings)

    # Y var(s)
    split_angle = 30
    stem_length = 50
    split_length = 25

    Draw_Snow_Flake(turtle)

    turtle.penup()


# Exercise 1.5 : Spruce up drawing from Exercise 1.4
def Exercise_One_Five(turtle):
    
    Turtle_Reset(turtle, 0, 0)

    # Fucntions
    def DrawY(t):
        turtle.forward(stem_length)

        x = t.xcor()
        y = t.ycor()

        t.left(split_angle)
        t.forward(split_length)
        t.right(split_angle)

        t.penup()
        t.goto(x, y)
        t.pendown()

        turtle.begin_fill()
        t.right(split_angle)
        t.forward(split_length)
        t.left(split_angle)

    def Draw_Snow_Flake(t):
        wings = 7

        x = t.xcor()
        y = t.ycor()

        for _ in range(wings):
            turtle.color('blue', 'green')
            DrawY(t)
            t.goto(x, y)
            turtle.end_fill()
            t.left(360 / wings)

    # Y var(s)
    split_angle = 30
    stem_length = 50
    split_length = 25

    Draw_Snow_Flake(turtle)

    turtle.penup()
    
main()

turtle.Screen().exitonclick()