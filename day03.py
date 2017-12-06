#!/usr/bin/env python
"""Day 03 of advent of code"""

DATA = 325489


def get_coordinates(data, value, step, direction, current_x, current_y):
    """Function for looping until correct coordinate is found"""
    while value <= data:
        for _ in range(0, 2):
            for _ in range(0, step):
                value += 1
                # Step
                if direction == 0:
                    current_x += 1
                elif direction == 1:
                    current_y += 1
                elif direction == 2:
                    current_x -= 1
                elif direction == 3:
                    current_y -= 1

                if value == data:
                    return (current_x, current_y)
            # Change direction
            direction = (direction + 1) % 4
        # Increase steps
        step += 1


# Part one
COORDINATES = get_coordinates(DATA, 1, 1, 0, 0, 0)

DISTANCE_X = abs(0 - COORDINATES[0])
DISTANCE_Y = abs(0 - COORDINATES[1])

DISTANCE = DISTANCE_X + DISTANCE_Y

print DISTANCE

# Part two


def get_value_larger(data, value, step, direction, size_x, size_y):
    """Function for looping until correct coordinate is found"""
    matrix = [[0 for _ in range(size_x)] for _ in range(size_y)]
    current_x = size_x / 2
    current_y = size_y / 2
    while value <= data:
        for _ in range(0, 2):
            for _ in range(0, step):
                matrix[current_x][current_y] = value
                # Step
                if direction == 0:
                    current_x += 1
                elif direction == 1:
                    current_y += 1
                elif direction == 2:
                    current_x -= 1
                elif direction == 3:
                    current_y -= 1

                value = matrix[current_x + 1][current_y] \
                    + matrix[current_x + 1][current_y + 1] \
                    + matrix[current_x][current_y + 1] \
                    + matrix[current_x - 1][current_y + 1] \
                    + matrix[current_x - 1][current_y] \
                    + matrix[current_x - 1][current_y - 1] \
                    + matrix[current_x][current_y - 1] \
                    + matrix[current_x + 1][current_y - 1]

                if value > data:
                    return value
            # Change direction
            direction = (direction + 1) % 4
        # Increase steps
        step += 1


VALUE = get_value_larger(325489, 1, 1, 0, 100, 100)
print VALUE
