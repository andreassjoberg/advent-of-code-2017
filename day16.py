#!/usr/bin/env python
"""Day 16 of advent of code"""


def swap(array, index_a, index_b):
    """Swaps two elements"""
    tmp = array[index_a]
    array[index_a] = array[index_b]
    array[index_b] = tmp


def part_one(data):
    """Part one"""
    array = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
             'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    commands = data.split(',')
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
    return ''.join(map(str, array))


def part_two(data):
    """Part two"""
    array = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
             'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    reverse_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6,
                    'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15}
    commands = data.split(',')
    for _ in range(1000000000 % 30):
        for command in commands:
            if command[0] == 's':
                spin_size = int(command[1:])
                for key, value in reverse_dict.iteritems():
                    reverse_dict[key] = (value + spin_size) % 16
                array = sorted(reverse_dict, key=reverse_dict.get)
            elif command[0] == 'x':
                index_a, index_b = command[1:].split('/')
                char_a, char_b = array[int(index_a)], array[int(index_b)]
                swap(array, int(index_a), int(index_b))
                swap(reverse_dict, char_a, char_b)
            elif command[0] == 'p':
                swap_a, swap_b = command[1:].split('/')
                index_a, index_b = reverse_dict[swap_a], reverse_dict[swap_b]
                swap(array, index_a, index_b)
                swap(reverse_dict, swap_a, swap_b)
    return ''.join(map(str, array))


if __name__ == '__main__':
    with open('day16.input', 'r') as f:
        INPUT_DATA = f.read()
    print part_one(INPUT_DATA)
    print part_two(INPUT_DATA)
