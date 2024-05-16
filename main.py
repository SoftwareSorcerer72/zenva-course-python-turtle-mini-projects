from turtle import *


speed(0)


move_distance = 20
setup(width=600, height=400)

bgcolor("#D2691E")

penup()
goto(100, 200)
pendown()


color("blue")
begin_fill()
goto(300, 200)
goto(300, -200)
goto(100, -200)
goto(100, 200)
end_fill()  

penup()
goto(-200, 0)
shape("turtle")
color("green")

def move_up():
    setheading(90)
    forward(move_distance)

move_up()


def move_down():
    setheading(270)
    forward(move_distance)

move_down()

def move_left():
    setheading(180)
    forward(move_distance)

move_left()

def move_right():
    setheading(0)
    forward(move_distance)
move_right()

onkey(move_up, "Up")
onkey(move_down, "Down")
onkey(move_left, "Left")
onkey(move_right, "Right")
listen()


done()














# START
# Set the background color to ORANGE
# Draw the ocean
# Move the turtle to starting position

# Pressed MOVE key?
#     Move turtle in that direction

#     Have we reached the goal?
#         Hide the turtle and disable controls
#         Write "YOU WIN!" on-screen

#         END









# https://www.codediagram.io/app/shares?token=a4eff907