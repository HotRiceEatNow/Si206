# Your name: Jason Le       
# Your student id: 4025 2793    
# Your email:lejaso@umich.edu
# List who or what you worked with on this homework:
# If you used Generative AI, say that you used it and also how you used it.

from turtle import *

### WRITE ALL NEW FUNCTIONS HERE ###

def draw_circle(turtle,x_in,y_in, radius): # drawring a cricle at the coordinate desire
    turtle.penup()
    turtle.goto(x_in, y_in - radius)
    turtle.pendown()
    turtle.color("yellow")
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
def draw_rectangle(turtle, xpos, ypos, width, height, color, size): # drawing a rectangle with x and y and color and size
    turtle.penup()
    turtle.goto(xpos, ypos)
    turtle.pendown()
    turtle.color(color)
    turtle.pensize(size)
    turtle.begin_fill()
    for x in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def draw_triangle(turtle, xpos, ypos, color,length_in, condition_in):   
    turtle.penup()
    turtle.goto(xpos, ypos)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.left(60)
    turtle.forward(length_in)
    turtle.right(120)
    turtle.forward(length_in)
    if condition_in == 1:
        turtle.penup()
    turtle.right(120)
    turtle.forward(length_in)
    turtle.end_fill()
def draw_emoji(turtle):
    """
    Write a function to draw your favorite or most frequently used emoji using the passed turtle.
    """
    # drawing a big face first
    draw_circle(turtle, 0, 0, 100)

    # drawing the eyes
    draw_rectangle(turtle, -60, 40, 40, 10, "black", 1)
    draw_rectangle(turtle, 20, 40, 40, 10, "black", 1)

    # drawing the mouth
    draw_triangle(turtle, -40, -30, "blue",30, 1)
    



def main():
 
    space = Screen()
    jason = Turtle()
    space.bgcolor("lightblue") 
    draw_emoji(jason)
   
    space.exitonclick()



if __name__ == '__main__':
    main()