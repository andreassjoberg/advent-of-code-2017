#!/usr/bin/env python
"""Day 06 of advent of code"""

DATA = r'14	0	15	12	11	11	3	5	1	6	8	4	9	1	8	4'

PREVIOUS = []
CURRENT = map(int, DATA.split())


def exists(array, previous_arrays):
    """Tests if the array has been seen before"""
    for i in previous_arrays:
        if array == i:
            return True
    return False


CYCLES = 0
while not exists(CURRENT, PREVIOUS):
    CYCLES += 1
    PREVIOUS.append(CURRENT[:])
    MAX = max(CURRENT)
    INDEX = CURRENT.index(MAX)
    BLOCKS = CURRENT[INDEX]
    CURRENT[INDEX] = 0
    for j in range(0, BLOCKS):
        SPREAD_INDEX = (INDEX + 1 + j) % len(CURRENT)
        CURRENT[SPREAD_INDEX] = CURRENT[SPREAD_INDEX] + 1

print CYCLES
