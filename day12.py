#!/usr/bin/env python
"""Day 12 of advent of code"""


def add_connected_to(data, connected):
    """Adds connected to"""
    for line in data.splitlines():
        left, right = line.split(" <-> ")
        if left in connected:
            connected.append(left)
            for elem in right.split(", "):
                connected.append(elem)
        for elem in right.split(", "):
            if elem in connected:
                connected.append(left)
                connected.append(elem)


def part_one(data):
    """Part one"""
    connected_to_zero = ["0"]
    length = 0
    previous_length = -1
    while previous_length != length:
        previous_length = length
        add_connected_to(data, connected_to_zero)
        length = len(set(connected_to_zero))
    return length


def update_group(elems, groups):
    """Updates group with elems"""
    for group in groups:
        for elem in elems:
            if elem in group:
                for e in elems:
                    if e not in group:
                        group.append(e)
                return
    groups.append(elems)


def merge_groups(i, j, groups):
    """Merges two groups"""
    for elem in groups[j]:
        if elem not in groups[i]:
            groups[i].append(elem)
    del groups[j]


def link_duplicates(groups):
    """Links and removes duplicates"""
    for i in range(len(groups)):
        for elem in groups[i]:
            for j in range(len(groups)):
                if i != j:
                    if elem in groups[j]:
                        merge_groups(i, j, groups)
                        return True
    return False


def part_two(data):
    """Part two"""
    groups = [[]]
    for line in data.splitlines():
        left, right = line.split(" <-> ")
        elems = map(int, right.split(", "))
        elems.append(int(left))
        update_group(elems, groups)
    groups = groups[1:]
    while link_duplicates(groups):
        pass
    return len(groups)


if __name__ == '__main__':
    with open('day12.input', 'r') as f:
        INPUT_DATA = f.read()
    print part_one(INPUT_DATA)
    print part_two(INPUT_DATA)
