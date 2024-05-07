# Be able to detect inputs.
# Require multiple inputs to pop the ballon.
# Utilize variables, conditions and functions.

#Code Diagram for project below 

# https://www.codediagram.io/app/shares?token=a645c4a9

# pseudo code

# Start 
# Draw the balloon 
# Has the key been pressed? 
#     Has the ballon reached max size? 
#         Clear the ballon
#     If not 
#         Increase the balloon size
#         Draw the balloon
# End


from turtle import *

diameter = 40
pop_diameter =100

def draw_balloon():
    color("red")
    dot(diameter)

def inflate_balloon():
    global diameter
    diameter = diameter + 10
    draw_balloon()

    if diameter >= pop_diameter:
        clear()
        diameter = 40
        write("POP!")




draw_balloon()

onkey(inflate_balloon, "Up")
listen()

done()