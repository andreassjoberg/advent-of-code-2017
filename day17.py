#!/usr/bin/env python
"""Day 17 of advent of code"""


def part_one():
    """Part one"""
    step = 386
    rounds = 2017
    state = [0]
    current_position = 0
    for i in range(rounds):
        boundary = len(state)
        current_position = ((current_position + step) % boundary) + 1
        state.insert(current_position, i + 1)
    return state[current_position + 1]


def part_two():
    """Part two"""
    step = 386
    rounds = 50000000
    length = 0
    zero_position = current_position = 0
    target = 0
    for i in range(rounds):
        length += 1
        current_position = ((current_position + step) % length) + 1
        if current_position == zero_position:
            zero_position += 1
        elif current_position == (zero_position + 1) % length:
            target = i + 1
    return target


if __name__ == '__main__':
    print part_one()
    print part_two()
