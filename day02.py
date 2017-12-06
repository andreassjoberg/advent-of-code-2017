#!/usr/bin/env python
"""Day 02 of advent of code"""


def part_one(data):
    """Part one"""
    checksum = 0
    for row in data.splitlines():
        numbers = map(int, row.split())
        largest = max(numbers)
        smallest = min(numbers)
        checksum += largest - smallest
    return checksum


def part_two(data):
    """Part two"""
    checksum = 0
    for row in data.splitlines():
        numbers = map(int, row.split())
        for i in range(0, len(numbers)):
            for j in range(0, len(numbers)):
                if i != j:
                    if numbers[i] % numbers[j] == 0:
                        checksum += numbers[i] / numbers[j]
    return checksum


if __name__ == '__main__':
    with open('day02.input', 'r') as f:
        INPUT_DATA = f.read()
    print part_one(INPUT_DATA)
    print part_two(INPUT_DATA)
