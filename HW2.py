# Your name: Jason Le       
# Your student id: 4025 2793
# Your email: lejaso@umich.edu
# List who or what you worked with on this homework:
# If you used Generative AI, say that you used it and also how you used it.
import random
from turtle import *

### WRITE ALL NEW FUNCTIONS HERE ###

def draw_rectangle(turtle, xpos, ypos, width, height, color): # drawing a rectangle with x and y and color and size
    turtle.penup()
    turtle.goto(xpos, ypos)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for x in range(2): # loop to go right then down then left then up to make a rec
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def draw_circle(turtle,x_in,y_in, color,radius): # drawring a cricle at the coordinate desire
    turtle.penup()
    turtle.goto(x_in, y_in - radius)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
# function to draw a triangle
def draw_triangle(turtle, xpos, ypos, color,length_in,length_bot):   
    turtle.penup()
    turtle.goto(xpos, ypos)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.left(60)
    turtle.forward(length_in)
    turtle.right(120)
    turtle.forward(length_in)
    turtle.right(120)
    turtle.forward(length_bot)
    turtle.end_fill()
#making snowflakes
def draw_snowflake(turtle, x, y, size): 
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("white")
    for _ in range(8):  # loop to draw snow flake with 8 lines
        turtle.forward(size)
        turtle.backward(size)
        turtle.right(45)

# my name function
def draw_J(turtle, x, y, color):  # Draw J
    draw_rectangle(turtle, x, y, 5, 30, color)  # the straight shape
    draw_rectangle(turtle, x - 15, y - 30, 20, 5, color)  # the bottom 

def draw_L(turtle, x, y, color):  # Draw  L
    draw_rectangle(turtle, x, y, 5, 30, color)  #  line
    draw_rectangle(turtle, x, y - 30, 20, 5, color)  #  base
def draw_winter_scene(turtle):
    """
    Write a function to draw a winter scene using the passed turtle.

    You can earn extra credit for including you initials (in block letters) in your drawing.
    See the instructions for more details.
    """

    # Drawing the bottom of the snowman 
    draw_circle(turtle, 0, -60, "white", 90)  

    # Drawing the bodfy of the snowman
    draw_circle(turtle, 0, 0, "white", 60) 

    # Drawing the head of the snowman
    draw_circle(turtle, 0, 60, "white", 30)  
    draw_circle(turtle, 0, 90, "green", 8)  # beanie

    # Drawing the eyes
    draw_rectangle(turtle, -15, 75, 5, 5, "black")  # left eye
    draw_rectangle(turtle, 10, 75, 5, 5, "black")  # right eye

    # Drawing the mouth
    draw_rectangle(turtle, -10, 65, 20, 2, "black") 

    # Drawing the snowman's arms 
    turtle.penup()
    turtle.goto(-60, 0)  # left arm
    turtle.pendown()
    turtle.color("brown")
    turtle.width(5)
    turtle.goto(-100, 40) 

    turtle.penup()
    turtle.goto(60, 0)  # right arm
    turtle.pendown()
    turtle.goto(100, 40) 

    # here ur snow
    for _ in range(50): #making 30 snow flakes
        x = random.randint(-500, 500)  # in random x coor
        y = random.randint(-500, 500)  # and in random y coor
        size = random.randint(5, 15)  # and since snow has random size, here to make it more real ehhe
        draw_snowflake(turtle, x, y, size)
    # siginging with my jl
    draw_J(turtle, -50, -160, "blue")  
    draw_L(turtle, 20, -160, "blue")  
def main():
    """
    Make sure to create a Screen object, a Turtle object,
    and call draw_winter_scene.

    Also, make sure to call the .exitonclick() method on your Screen instance
    to stop the program from exiting until you close the drawing window.

    TIP: You can call the .bgcolor() method on your Screen instance to change
    the background color.
    """

    space = Screen()
    jason = Turtle()
    space.bgcolor("lightblue") 
    draw_winter_scene(jason)
   
    space.exitonclick()



if __name__ == '__main__':
    main()