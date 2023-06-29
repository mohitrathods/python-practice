""""""
"""
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. 
The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. 
If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2
"""

import math
#initialize curr pos
x,y = 0,0

# print(round(math.sqrt(10)))
while True:
    #get movements directions and steps
    movements = input().split()
    if not movements:
        break

    direction = movements[0] #movements = ['UP',3]
    steps = int(movements[1])

    #update current pos based on the movement
    if direction == 'UP':
        y += steps
    elif direction == 'DOWN':
        y -= steps
    elif direction == 'LEFT':
        y -= steps
    elif direction == 'RIGHT':
        y += steps

distance = math.sqrt(x ** 2+y ** 2)
print(round(distance))


"""
In this program, we initialize the current position at (0, 0) and then process the movement sequence using a while loop. Each movement is split into direction and 
steps using split().

Based on the direction, the current position (x, y) is updated accordingly. Moving "UP" increases the y-coordinate, moving "DOWN" decreases the y-coordinate, moving 
"LEFT" decreases the x-coordinate, and moving "RIGHT" increases the x-coordinate.

After processing all the movements, we compute the distance from the current position to the original point using the Euclidean distance formula. 
The math.sqrt() function is used to calculate the square root, and round() is used to round the distance to the nearest integer.
"""