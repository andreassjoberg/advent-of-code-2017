#!/usr/bin/env python
"""Day 08 of advent of code"""


def part_one(data):
    """Part one"""
    variables = {}
    for line in data.splitlines():
        commands = line.split(' ')
        variables[commands[0]] = 0
    for line in data.splitlines():
        commands = line.split(' ')
        operator = commands[5]
        if commands[1] == 'inc':
            value = 1
        else:
            value = -1
        if operator == '>':
            if variables[commands[4]] > int(commands[6]):
                variables[commands[0]] += value * int(commands[2])
        elif operator == '>=':
            if variables[commands[4]] >= int(commands[6]):
                variables[commands[0]] += value * int(commands[2])
        elif operator == '<':
            if variables[commands[4]] < int(commands[6]):
                variables[commands[0]] += value * int(commands[2])
        elif operator == '<=':
            if variables[commands[4]] <= int(commands[6]):
                variables[commands[0]] += value * int(commands[2])
        elif operator == '==':
            if variables[commands[4]] == int(commands[6]):
                variables[commands[0]] += value * int(commands[2])
        elif operator == '!=':
            if variables[commands[4]] != int(commands[6]):
                variables[commands[0]] += value * int(commands[2])
    return variables[max(variables, key=variables.get)]


def part_two(data):
    """Part two"""
    variables = {}
    maximum = 0
    for line in data.splitlines():
        commands = line.split(' ')
        variables[commands[0]] = 0
    for line in data.splitlines():
        commands = line.split(' ')
        operator = commands[5]
        if commands[1] == 'inc':
            value = 1
        else:
            value = -1
        if operator == '>':
            if variables[commands[4]] > int(commands[6]):
                variables[commands[0]] += value * int(commands[2])
        elif operator == '>=':
            if variables[commands[4]] >= int(commands[6]):
                variables[commands[0]] += value * int(commands[2])
        elif operator == '<':
            if variables[commands[4]] < int(commands[6]):
                variables[commands[0]] += value * int(commands[2])
        elif operator == '<=':
            if variables[commands[4]] <= int(commands[6]):
                variables[commands[0]] += value * int(commands[2])
        elif operator == '==':
            if variables[commands[4]] == int(commands[6]):
                variables[commands[0]] += value * int(commands[2])
        elif operator == '!=':
            if variables[commands[4]] != int(commands[6]):
                variables[commands[0]] += value * int(commands[2])
        maximum = max(variables[max(variables, key=variables.get)], maximum)
    return maximum


if __name__ == '__main__':
    with open('day08.input', 'r') as f:
        INPUT_DATA = f.read()
    print part_one(INPUT_DATA)
    print part_two(INPUT_DATA)
