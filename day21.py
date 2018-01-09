#!/usr/bin/env python
"""Day 21 of advent of code"""

from math import sqrt
from os import linesep


def read_rules(data):
    """Reads rules into structure"""
    rules = []
    for line in data.splitlines():
        in_pattern, out_pattern = line.split(' => ')
        in_rule, out_rule = [], []
        for row in in_pattern.split('/'):
            in_rule.append(list(row))
        for row in out_pattern.split('/'):
            out_rule.append(list(row))
        rules.append((in_rule, out_rule))
    return rules


def rule_is_match(rule, image):
    """True if rule is match"""
    if isinstance(image[0][0], list):
        pass
    else:
        if len(rule) == len(image):
            if len(rule[0]) == len(image[0]):
                for i in range(len(image)):
                    for j in range(len(image[i])):
                        if rule[i][j] != image[i][j]:
                            return False
                return True
    return False


def apply_rule(rule):
    """Applies rule to image"""
    return rule


def flip(rule):
    """Flips the rule"""
    for row in range(len(rule)):
        for column in range(len(rule[row]) / 2):
            temp = rule[row][column]
            rule[row][column] = rule[row][len(rule[row]) - 1 - column]
            rule[row][len(rule[row]) - 1 - column] = temp


def rotate(rule):
    """Rotates rule 90 degrees clockwise"""
    length = len(rule)
    for x in range(length / 2):
        for y in range(x, length - 1 - x):
            tmp = rule[length - 1 - y][x]
            rule[length - 1 - y][x] = rule[length - 1 - x][length - 1 - y]
            rule[length - 1 - x][length - 1 - y] = rule[y][length - 1 - x]
            rule[x][y] = rule[y][length - 1 - x] = rule[x][y]
            rule[x][y] = tmp


def do_rule(rules, image):
    """Performs rule"""
    if isinstance(image[0][0], list):
        for section in range(len(image)):
            image[section] = do_rule(rules, image[section])
    else:
        for in_rule, out_rule in rules:
            if len(in_rule) != len(image):
                continue
            for rotation in range(4):
                if rotation > 0:
                    rotate(in_rule)
                for _ in range(2):
                    if rule_is_match(in_rule, image):
                        return apply_rule(out_rule)
                    flip(in_rule)
    return image


def split_image(image):
    """Splits image into grid"""
    lines = image.splitlines()
    length = len(lines[0])
    if length % 2 == 0:
        block_size = 2
    else:
        block_size = 3
    num_blocks = length / block_size
    new_image = []
    for y in range(num_blocks):
        for x in range(num_blocks):
            if block_size == 2:
                block = [[lines[y * block_size][x * block_size],
                          lines[y * block_size][x * block_size + 1]],
                         [lines[y * block_size + 1][x * block_size],
                          lines[y * block_size + 1][x * block_size + 1]]]
            elif block_size == 3:
                block = [[lines[y * block_size][x * block_size],
                          lines[y * block_size][x * block_size + 1],
                          lines[y * block_size][x * block_size + 2]],
                         [lines[y * block_size + 1][x * block_size],
                          lines[y * block_size + 1][x * block_size + 1],
                          lines[y * block_size + 1][x * block_size + 2]],
                         [lines[y * block_size + 2][x * block_size],
                          lines[y * block_size + 2][x * block_size + 1],
                          lines[y * block_size + 2][x * block_size + 2]]]
            new_image.append(block)
    return new_image


def merge_image(image):
    """Merges grids into image"""
    new_image = []
    if isinstance(image[0][0], list):
        length = int(sqrt(len(image)))
        for block_y in range(length):
            for row in range(len(image[block_y])):
                entire_row = ''
                for column in range(length):
                    entire_row += ''.join(image[block_y * length + column]
                                          [row])
                new_image.append(list(entire_row))
        str_image = ''
        for row in new_image:
            str_image += ''.join(row) + linesep
        return str_image
    raise AssertionError


def part_one(data):
    """Part one"""
    image = """.#.
..#
###"""
    rules = read_rules(data)
    for i in range(5):
        image = split_image(image)
        image = do_rule(rules, image)
        image = merge_image(image)
    return image.count('#')


def part_two(data):
    """Part two"""
    image = """.#.
..#
###"""
    rules = read_rules(data)
    for i in range(18):
        image = split_image(image)
        image = do_rule(rules, image)
        image = merge_image(image)
    return image.count('#')


if __name__ == '__main__':
    with open('day21.input', 'r') as f:
        INPUT_DATA = f.read()
    print part_one(INPUT_DATA)
    print part_two(INPUT_DATA)
