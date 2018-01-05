#!/usr/bin/env python
"""Day 23 of advent of code"""

from collections import defaultdict


def get_value(registers, register):
    """Gets the value"""
    if register >= 'a' and register <= 'z':
        return registers[register]
    return int(register)


def part_one(data):
    """Part one"""
    num_mult = 0
    registers = defaultdict(int)
    lines = data.splitlines()
    i = 0
    while i < len(lines):
        instr, val_a, val_b = lines[i].split(' ')
        if instr == 'set':
            registers[val_a] = get_value(registers, val_b)
        elif instr == 'sub':
            registers[val_a] = registers[val_a] - get_value(registers, val_b)
        elif instr == 'mul':
            num_mult += 1
            registers[val_a] = registers[val_a] * get_value(registers, val_b)
        elif instr == 'jnz':
            if get_value(registers, val_a) != 0:
                i += get_value(registers, val_b)
                continue
        i += 1
    return num_mult


def part_two():
    """Part two"""
    register_b = 106700
    register_c = 123700
    register_h = 0
    while register_b <= register_c:
        register_f = 1
        for register_d in range(2, register_b / 2):
            if register_b % register_d == 0:
                register_f = 0
                break
        if register_f == 0:
            register_h += 1
        register_b += 17
    return register_h


if __name__ == '__main__':
    with open('day23.input', 'r') as f:
        INPUT_DATA = f.read()
    print part_one(INPUT_DATA)
    print part_two()
