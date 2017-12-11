#!/usr/bin/env python
"""Day 10 of advent of code"""


def part_one(data):
    """Part one"""
    rope_length = 256
    rope = []
    for i in range(rope_length):
        rope.append(i)
    current_position = skip_size = 0
    for elem in data.split(","):
        length = int(elem)
        sub_list = []
        for i in range(length):
            sub_list.append(rope[(current_position + i) % rope_length])
        sub_list.reverse()
        for i in range(length):
            rope[(current_position + i) % rope_length] = sub_list[i]
        current_position += (length + skip_size) % rope_length
        skip_size += 1
    return rope[0] * rope[1]


def part_two(data):
    """Part two"""
    lengths = [ord(x) for x in data]
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


if __name__ == '__main__':
    with open('day10.input', 'r') as f:
        INPUT_DATA = f.read()
    print part_one(INPUT_DATA)
    print part_two(INPUT_DATA)
