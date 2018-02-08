
##########
### The below Python code is copyrighted by Lusi Yang. ###
### Contact: lusiyang@gmail.com or lusi.yang@mail.utoronto.ca ###
### Actual Program: http://bit.ly/2EQygrK ###
### Copyright © 2017 ###
##########

import turtle
import random

# name of the game
screen = turtle.Screen()
screen.title('Rat Game for Cats')

# the size of the game screen
screen_width = 600
screen_height = 600
turtle.setup(screen_width, screen_height)

# the rat
rat = turtle.Turtle()
screen.register_shape("rat.gif")
rat.shape("rat.gif")
rat.penup()
rat.speed(8)
rat.setheading(120)

def headIntoCanvas(rat):
    """ keep turtle on canvas """
    xmin = -screen_width / 2
    xmax = screen_width / 2
    ymin = -screen_height / 2
    ymax = screen_height / 2

    xcor, ycor = rat.position()

    old_heading = rat.heading()

    if not xmin < xcor < xmax:
        new_heading = (180 - old_heading)
        return new_heading  # bounce off left or right wall

    if not ymin < ycor < ymax:
        new_heading = (360 - old_heading)
        return new_heading  # bounce off floor or ceiling

    return old_heading  # stay the course

# the rat movement
def move():
    rat.forward(5)
    rat.setheading(headIntoCanvas(rat))
    turtle.ontimer(move, 25) # makes the turtle march around
move()

# exit on close window 
turtle.exitonclick()
