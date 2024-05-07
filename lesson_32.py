from turtle import *



# def move_and_turn (angle):
#     num = 0
#     for x in range(8):
#         num = num + 1
#         forward(50)
#         right(angle)


# move_and_turn(45) 

def move_and_turn (angle):
    forward(50)
    right(angle)

for x in range(12):
    move_and_turn(30)



done()