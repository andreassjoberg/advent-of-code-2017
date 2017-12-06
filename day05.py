#!/usr/bin/env python
"""Day 05 of advent of code"""


def part_one(data):
    """Part one"""
    instructions = map(int, data.splitlines())
    current_index = 0
    steps_taken = 0
    while current_index < len(instructions):
        jump = instructions[current_index]
        instructions[current_index] = instructions[current_index] + 1
        current_index += jump
        steps_taken += 1
    return steps_taken


def part_two(data):
    """Part two"""
    instructions = map(int, data.splitlines())
    current_index = 0
    steps_taken = 0
    while current_index < len(instructions):
        jump = instructions[current_index]
        if instructions[current_index] >= 3:
            instructions[current_index] = instructions[current_index] - 1
        else:
            instructions[current_index] = instructions[current_index] + 1
        current_index += jump
        steps_taken += 1
    return steps_taken


if __name__ == '__main__':
    with open('day05.input', 'r') as f:
        INPUT_DATA = f.read()
    print part_one(INPUT_DATA)
    print part_two(INPUT_DATA)
