#!/usr/bin/env python
"""Day 15 of advent of code"""


def generate_next_number(previous, factor, multiple):
    """Generates next number in sequence"""
    while True:
        value = (previous * factor) % 2147483647
        if value % multiple == 0:
            return value
        previous = value


def count_collitions(data, rounds, multiples):
    """Count number of collitions"""
    factors = [16807, 48271]
    start = map(int, data.split(","))
    previous = start[:]
    matches = 0
    for i in range(rounds):
        gen_a = generate_next_number(previous[0], factors[0], multiples[0])
        gen_b = generate_next_number(previous[1], factors[1], multiples[1])
        previous = gen_a, gen_b
        if (gen_a & 65535) == (gen_b & 65535):
            matches += 1
    return matches


def part_one(data):
    """Part one"""
    return count_collitions(data, 40000000, [1, 1])


def part_two(data):
    """Part two"""
    return count_collitions(data, 5000000, [4, 8])


if __name__ == '__main__':
    with open('day15.input', 'r') as f:
        INPUT_DATA = f.read()
    print part_one(INPUT_DATA)
    print part_two(INPUT_DATA)
