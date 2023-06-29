import math

# Initialize the current position
x = 0
y = 0

# Process the movement sequence
while True:
    # Get the movement direction and steps
    movement = input().split()
    if not movement:
        break

    direction = movement[0]
    steps = int(movement[1])

    # Update the current position based on the movement
    if direction == 'UP':
        y += steps
    elif direction == 'DOWN':
        y -= steps
    elif direction == 'LEFT':
        x -= steps
    elif direction == 'RIGHT':
        x += steps

# Compute the distance from the current position to the original point
distance = math.sqrt(x ** 2 + y ** 2)

# Print the nearest integer distance
print(round(distance))
