#!/usr/bin/env python
"""Day 09 of advent of code"""


TOTAL_SCORE = 0


def find_closing_bracket(data, i, score):
    """Finds the closing bracket in data"""
    global TOTAL_SCORE
    in_garbage = False
    j = i
    while j < len(data):
        if data[j] == "{" and not in_garbage:
            j = find_closing_bracket(data, j + 1, score + 1)
        elif data[j] == "}" and not in_garbage:
            TOTAL_SCORE += score
            return j
        elif data[j] == "!":
            j += 1
        elif data[j] == "<" and not in_garbage:
            in_garbage = True
        elif data[j] == ">" and in_garbage:
            in_garbage = False
        j += 1


def part_one(data):
    """Part one"""
    global TOTAL_SCORE
    in_garbage = False
    j = 0
    while j < len(data):
        if data[j] == "{" and not in_garbage:
            j = find_closing_bracket(data, j + 1, 1)
        elif data[j] == "}" and not in_garbage:
            TOTAL_SCORE += 1
            return j
        elif data[j] == "!":
            j += 1
        elif data[j] == "<" and not in_garbage:
            in_garbage = True
        elif data[j] == ">" and in_garbage:
            in_garbage = False
        j += 1
    return TOTAL_SCORE


def part_two(data):
    """Part two"""
    in_garbage = False
    garbage = 0
    i = 0
    while i < len(data):
        if data[i] == "!":
            i += 1
        elif data[i] == "<" and not in_garbage:
            in_garbage = True
        elif data[i] == ">" and in_garbage:
            in_garbage = False
        elif in_garbage:
            garbage += 1
        i += 1
    return garbage


if __name__ == '__main__':
    with open('day09.input', 'r') as f:
        INPUT_DATA = f.read()
    print part_one(INPUT_DATA)
    print part_two(INPUT_DATA)
