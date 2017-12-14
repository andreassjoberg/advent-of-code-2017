#!/usr/bin/env python
"""Day 14 of advent of code"""


def knot_hash(string):
    """Calculates the knot hash"""
    lengths = [ord(x) for x in string]
    lengths.extend([17, 31, 73, 47, 23])
    rope = [x for x in range(0, 256)]
    rope_length = len(rope)
    current_position = skip_size = 0
    for _ in range(64):
        for length in lengths:
            sub_list = []
            for i in range(length):
                sub_list.append(rope[(current_position + i) % rope_length])
            sub_list.reverse()
            for i in range(length):
                rope[(current_position + i) % rope_length] = sub_list[i]
            current_position += (length + skip_size) % rope_length
            skip_size += 1
    xor_hash = []
    for i in range(16):
        xor = 0
        for j in range(16):
            xor ^= rope[i * 16 + j]
        xor_hash.append(xor)
    result = ""
    for xor in xor_hash:
        result += format(xor, '02x')
    return result


def part_one(data):
    """Part one"""
    ones = 0
    for i in range(128):
        input_data = "%s-%d" % (data, i)
        input_hash = knot_hash(input_data)
        row = ""
        for j in range(0, 32, 2):
            row += "{0:08b}".format(int(input_hash[j:j + 2], 16))
        for char in row:
            if char == "1":
                ones += 1
    return ones


def mark_adjacent(grid, x, y):
    """Marks adjacent cells as same region"""
    grid[x] = "%sX%s" % (grid[x][:y], grid[x][y + 1:])
    if x - 1 >= 0 and grid[x - 1][y] == "#":
        mark_adjacent(grid, x - 1, y)
    if x + 1 < len(grid) and grid[x + 1][y] == "#":
        mark_adjacent(grid, x + 1, y)
    if y - 1 >= 0 and grid[x][y - 1] == "#":
        mark_adjacent(grid, x, y - 1)
    if y + 1 < len(grid[x]) and grid[x][y + 1] == "#":
        mark_adjacent(grid, x, y + 1)


def part_two(data):
    """Part two"""
    grid = []
    for i in range(128):
        input_data = "%s-%d" % (data, i)
        input_hash = knot_hash(input_data)
        row = ""
        for j in range(0, 32, 2):
            row += "{0:08b}".format(int(input_hash[j:j + 2], 16))
        grid.append(row.replace("0", ".").replace("1", "#"))
    region = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == "#":
                region += 1
                mark_adjacent(grid, x, y)
    return region


if __name__ == '__main__':
    with open('day14.input', 'r') as f:
        INPUT_DATA = f.read()
    print part_one(INPUT_DATA)
    print part_two(INPUT_DATA)
