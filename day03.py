#!/usr/bin/env python
"""Day 03 of advent of code"""

# Part one


def get_coordinates(threshold, value, step, direction, current_x, current_y):
    """Function for looping until correct coordinate is found"""
    while value <= threshold:
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

                if value == threshold:
                    return (current_x, current_y)
            # Change direction
            direction = (direction + 1) % 4
        # Increase steps
        step += 1


def part_one(data):
    """Part one"""
    coordinates = get_coordinates(data, 1, 1, 0, 0, 0)
    distance_x = abs(0 - coordinates[0])
    distance_y = abs(0 - coordinates[1])
    distance = distance_x + distance_y
    return distance

# Part two


def get_value_larger(threshold, value, step, direction, size_x, size_y):
    """Function for looping until correct coordinate is found"""
    matrix = [[0 for _ in range(size_x)] for _ in range(size_y)]
    current_x = size_x / 2
    current_y = size_y / 2
    while value <= threshold:
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

                if value > threshold:
                    return value
            # Change direction
            direction = (direction + 1) % 4
        # Increase steps
        step += 1


def part_two(data):
    """Part two"""
    return get_value_larger(data, 1, 1, 0, 100, 100)


if __name__ == '__main__':
    INPUT_DATA = 325489
    print part_one(INPUT_DATA)
    print part_two(INPUT_DATA)
