from turtle import *
from random import *

speed(0)

bgcolor("black")
hideturtle()
width = window_width()
height = window_height()

def draw_star(xpos, ypos):
    size = randrange(1, 10)
    penup()
    goto(xpos, ypos)
    pendown()
    dot(size, "white")


for x in range (1000):
    xpos = randrange(-width // 2, width // 2)
    ypos = randrange(-height // 2, height // 2)
    draw_star(xpos, ypos)



done()






















# START
# Set the background color to BLACK
# Repeat 100 times
#     Generate random star position
#     Generate random star size
#     Draw the star
# END






#https://www.codediagram.io/app/shares?token=d12ec055