#!/usr/bin/env python
"""Day 22 of advent of code"""


def build_grid(input_lines, size):
    """Builds grid"""
    grid = []
    for y in range(size):
        row = []
        for x in range(size):
            row.append('.')
        grid.append(row)
    input_length = len(input_lines[0])
    start_x = start_y = (size / 2) - (input_length / 2)
    for y in range(input_length):
        for x in range(len(input_lines[y])):
            grid[start_y + y][start_x + x] = input_lines[y][x]
    return grid


def print_grid(grid, current_x, current_y):
    """Prints grid"""
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if y == current_y and x == current_x:
                print '[' + grid[y][x] + ']',
            else:
                print ' ' + grid[y][x] + ' ',
        print


def part_one(data):
    """Part one"""
    size = 1000
    grid = build_grid(data.splitlines(), size)
    current_x = current_y = size / 2
    num_infections = 0
    #   0
    # 1   3
    #   2
    direction = 0
    for _ in range(10000):
        if grid[current_y][current_x] == '#':
            direction = (direction - 1) % 4
            grid[current_y][current_x] = '.'
        else:
            direction = (direction + 1) % 4
            grid[current_y][current_x] = '#'
            num_infections += 1
        if direction == 0:
            current_y -= 1
        elif direction == 1:
            current_x -= 1
        elif direction == 2:
            current_y += 1
        elif direction == 3:
            current_x += 1
    return num_infections


def part_two(data):
    """Part two"""
    size = 1000
    grid = build_grid(data.splitlines(), size)
    current_x = current_y = size / 2
    num_infections = 0
    #   0
    # 1   3
    #   2
    direction = 0
    for _ in range(10000000):
        if grid[current_y][current_x] == '#':
            direction = (direction - 1) % 4
            grid[current_y][current_x] = 'F'
        elif grid[current_y][current_x] == '.':
            direction = (direction + 1) % 4
            grid[current_y][current_x] = 'W'
        elif grid[current_y][current_x] == 'W':
            grid[current_y][current_x] = '#'
            num_infections += 1
        elif grid[current_y][current_x] == 'F':
            direction = (direction + 2) % 4
            grid[current_y][current_x] = '.'
        if direction == 0:
            current_y -= 1
        elif direction == 1:
            current_x -= 1
        elif direction == 2:
            current_y += 1
        elif direction == 3:
            current_x += 1
    return num_infections


if __name__ == '__main__':
    with open('day22.input', 'r') as f:
        INPUT_DATA = f.read()
    print part_one(INPUT_DATA)
    print part_two(INPUT_DATA)
