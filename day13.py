#!/usr/bin/env python
"""Day 13 of advent of code"""


def count_hits(level, length):
    """Count hits"""
    hits = 0
    for step in range(length + 1):
        if level.has_key(step):
            depth, rangee = step, level[step]
            if rangee == 1:
                hits += depth * rangee
            elif rangee > 1:
                divisor = 2 + (rangee - 2) * 2
                if step % divisor == 0:
                    hits += depth * rangee
    return hits


def caught(level, length, delay):
    """Returns true if you're caught"""
    for step in range(length + 1):
        if level.has_key(step):
            rangee = level[step]
            if rangee == 1:
                print "This can never be bypassed!"
                return True
            elif rangee > 1:
                divisor = 2 + (rangee - 2) * 2
                if (step + delay) % divisor == 0:
                    return True
    return False


def part_one(data):
    """Part one"""
    level = {}
    length = 0
    for line in data.splitlines():
        depth, rangee = line.split(": ")
        level[int(depth)] = int(rangee)
        length = max(length, int(depth))
    return count_hits(level, length)


def part_two(data):
    """Part two"""
    level = {}
    length = 0
    for line in data.splitlines():
        depth, rangee = line.split(": ")
        level[int(depth)] = int(rangee)
        length = max(length, int(depth))
    delay = 0
    while caught(level, length, delay):
        delay += 1
    return delay


if __name__ == '__main__':
    with open('day13.input', 'r') as f:
        INPUT_DATA = f.read()
    print part_one(INPUT_DATA)
    print part_two(INPUT_DATA)
