#!/usr/bin/env python
"""Day 01 of advent of code"""


def part_one(data):
    """Part one"""
    result = 0
    for i in range(1, len(data)):
        first = int(data[i - 1])
        second = int(data[i])
        if first == second:
            result += first
        while first == second and i < len(data) - 1:
            i += 1
            first = int(data[i - 1])
            second = int(data[i])
    if data[0] == data[len(data) - 1]:
        result += int(data[0])
    return result


def part_two(data):
    """Part two"""
    result = 0
    halfway_index = len(data) / 2
    for i in range(0, halfway_index):
        first = int(data[i])
        second = int(data[halfway_index + i])
        if first == second:
            result += first + second
    return result


if __name__ == '__main__':
    with open('day01.input', 'r') as f:
        INPUT_DATA = f.read()
    print part_one(INPUT_DATA)
    print part_two(INPUT_DATA)
