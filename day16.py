#!/usr/bin/env python
"""Day 16 of advent of code"""


def swap(array, index_a, index_b):
    """Swaps two elements"""
    tmp = array[index_a]
    array[index_a] = array[index_b]
    array[index_b] = tmp


def dance(array, commands):
    """Do the dance"""
    for command in commands:
        if command[0] == 's':
            spin_size = int(command[1:])
            for _ in range(spin_size):
                array.insert(0, array[-1])
                del array[-1]
        elif command[0] == 'x':
            index_a, index_b = command[1:].split('/')
            swap(array, int(index_a), int(index_b))
        elif command[0] == 'p':
            swap_a, swap_b = command[1:].split('/')
            index_a, index_b = array.index(swap_a), array.index(swap_b)
            swap(array, index_a, index_b)


def part_one(data):
    """Part one"""
    array = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
             'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    commands = data.split(',')
    dance(array, commands)
    return ''.join(map(str, array))


def part_two(data):
    """Part two"""
    array = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
             'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    commands = data.split(',')
    for _ in range(1000000000 % 30):
        dance(array, commands)
    return ''.join(map(str, array))


if __name__ == '__main__':
    with open('day16.input', 'r') as f:
        INPUT_DATA = f.read()
    print part_one(INPUT_DATA)
    print part_two(INPUT_DATA)
