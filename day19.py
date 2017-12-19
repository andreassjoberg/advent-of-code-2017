#!/usr/bin/env python
"""Day 19 of advent of code"""


def get_coordinates(current_x, current_y, direction, offset=1):
    """Gets next coordinates for direction"""
    if direction == 0:
        return (current_x, current_y - offset)
    elif direction == 1:
        return (current_x - offset, current_y)
    elif direction == 2:
        return (current_x, current_y + offset)
    elif direction == 3:
        return (current_x + offset, current_y)


def get_cell_value(grid, current_x, current_y, direction, offset=1):
    """Returns value of next position"""
    next_x, next_y = get_coordinates(
        current_x, current_y, direction, offset)
    return grid[next_y][next_x]


def can_walk_on_cell(grid, current_x, current_y, direction, offset=1):
    """Can offset on cell"""
    next_x, next_y = get_coordinates(current_x, current_y, direction, offset)
    if next_x < 0 or next_x >= len(grid[current_y]) \
            or next_y < 0 or next_y >= len(grid):
        return False
    cell_value = get_cell_value(grid, next_x, next_y, direction, 0)
    if direction % 2 == 0:
        path = '|'
    else:
        path = '-'
    return cell_value == path or cell_value == '+' \
        or (cell_value >= 'A' and cell_value <= 'Z') \
        or (cell_value != ' ' and get_cell_value(grid, current_x, current_y, direction, 2))


def get_direction(grid, current_x, current_y, direction):
    """Finds valid direction"""
    if can_walk_on_cell(grid, current_x, current_y, direction):
        return direction
    directions = [0, 1, 2, 3]
    directions.remove((direction + 2) % 4)
    for try_direction in directions:
        if can_walk_on_cell(grid, current_x, current_y, try_direction):
            return try_direction
    return direction


def move(grid, current_x, current_y, direction, collected):
    """Moves one position"""
    direction = get_direction(grid, current_x, current_y, direction)
    current_x, current_y = get_coordinates(
        current_x, current_y, direction)
    if can_walk_on_cell(grid, current_x, current_y, direction, 0):
        cell_value = get_cell_value(grid, current_x, current_y, direction, 0)
        collected.append(cell_value)
        return (current_x, current_y, direction, True)
    return (current_x, current_y, direction, False)


def run_forrest_run(data):
    """Do the thing"""
    grid = data.splitlines()
    current_y = 0
    current_x = grid[current_y].index('|')
    direction = 2
    collected = []
    moved = True
    while moved:
        current_x, current_y, direction, moved = move(
            grid, current_x, current_y, direction, collected)
    return collected


def part_one(data):
    """Part one"""
    collected = run_forrest_run(data)
    letters = []
    for char in collected:
        if char >= 'A' and char <= 'Z':
            letters.append(char)
    return ''.join(letters)


def part_two(data):
    """Part two"""
    collected = run_forrest_run(data)
    return len(collected) + 1


if __name__ == '__main__':
    with open('day19.input', 'r') as f:
        INPUT_DATA = f.read()
    print part_one(INPUT_DATA)
    print part_two(INPUT_DATA)
