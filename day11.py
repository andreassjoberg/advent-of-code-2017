#!/usr/bin/env python
"""Day 11 of advent of code"""


def count_steps(x, y):
    """Count steps back to 0,0"""
    steps_back = 0
    while x != 0 or y != 0:
        if x > 0:
            if y > 0:
                # sw
                y -= 1
            elif y < 0:
                # n
                x -= 1
                y += 1
            else:
                # nw
                x -= 1
        elif x < 0:
            if y > 0:
                # s
                x += 1
                y -= 1
            elif y < 0:
                # ne
                y += 1
            else:
                # se
                x += 1
        else:
            if y > 0:
                # sw
                y -= 1
            elif y < 0:
                # ne
                y += 1
            else:
                # don't move
                break
        steps_back += 1
    return steps_back


def part_one(data):
    """Part one"""
    commands = data.split(",")
    x = y = 0
    for command in commands:
        if command == "n":
            x -= 1
            y += 1
        elif command == "ne":
            y += 1
        elif command == "se":
            x += 1
        elif command == "s":
            x += 1
            y -= 1
        elif command == "sw":
            y -= 1
        elif command == "nw":
            x -= 1
    return count_steps(x, y)


def part_two(data):
    """Part two"""
    commands = data.split(",")
    x = y = 0
    max_steps = 0
    for command in commands:
        if command == "n":
            x -= 1
            y += 1
        elif command == "ne":
            y += 1
        elif command == "se":
            x += 1
        elif command == "s":
            x += 1
            y -= 1
        elif command == "sw":
            y -= 1
        elif command == "nw":
            x -= 1
        max_steps = max(max_steps, count_steps(x, y))
    return max_steps


if __name__ == '__main__':
    with open('day11.input', 'r') as f:
        INPUT_DATA = f.read()
    print part_one(INPUT_DATA)
    print part_two(INPUT_DATA)
