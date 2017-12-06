#!/usr/bin/env python
"""Day 06 of advent of code"""


def exists(array, previous_arrays):
    """Tests if the array has been seen before"""
    for i in previous_arrays:
        if array == i:
            return True
    return False


def part_one(data):
    """Part one"""
    previous = []
    current = map(int, data.split())
    cycles = 0
    while not exists(current, previous):
        cycles += 1
        previous.append(current[:])
        current_max = max(current)
        index = current.index(current_max)
        blocks = current[index]
        current[index] = 0
        for j in range(0, blocks):
            spread_index = (index + 1 + j) % len(current)
            current[spread_index] = current[spread_index] + 1
    return cycles


def part_two(data):
    """Part two"""
    previous = []
    current = map(int, data.split())
    cycles = 0
    while not exists(current, previous):
        cycles += 1
        previous.append(current[:])
        current_max = max(current)
        index = current.index(current_max)
        blocks = current[index]
        current[index] = 0
        for j in range(0, blocks):
            spread_index = (index + 1 + j) % len(current)
            current[spread_index] = current[spread_index] + 1
    previous = []
    cycles = 0
    while not exists(current, previous):
        cycles += 1
        previous.append(current[:])
        current_max = max(current)
        index = current.index(current_max)
        blocks = current[index]
        current[index] = 0
        for j in range(0, blocks):
            spread_index = (index + 1 + j) % len(current)
            current[spread_index] = current[spread_index] + 1
    return cycles


if __name__ == '__main__':
    with open('day06.input', 'r') as f:
        INPUT_DATA = f.read()
    print part_one(INPUT_DATA)
    print part_two(INPUT_DATA)
