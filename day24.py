#!/usr/bin/env python
"""Day 24 of advent of code"""


def build_bridges(connector, bridge, bridges, parts):
    """Builds possible brigdes"""
    possible_parts = []
    for part in parts:
        if part[0] == connector or part[1] == connector:
            possible_parts.append(part)
    for part in possible_parts:
        new_bridge = bridge[:]
        new_bridge.append(part)
        bridges.append(new_bridge)
        next_connector = part[0]
        if part[0] == connector:
            next_connector = part[1]
        remaining_parts = parts[:]
        remaining_parts.remove(part)
        build_bridges(next_connector, new_bridge, bridges, remaining_parts)
    return bridges


def part_one(data):
    """Part one"""
    parts = []
    for line in data.splitlines():
        port_a, port_b = map(int, line.split('/'))
        parts.append([port_a, port_b])
    bridges = build_bridges(0, [], [], parts)
    strongest_bridge = 0
    for bridge in bridges:
        strength = 0
        for port_a, port_b in bridge:
            strength += port_a + port_b
        strongest_bridge = max(strongest_bridge, strength)
    return strongest_bridge


def part_two(data):
    """Part two"""
    parts = []
    for line in data.splitlines():
        port_a, port_b = map(int, line.split('/'))
        parts.append([port_a, port_b])
    bridges = build_bridges(0, [], [], parts)
    strongest_bridge = 0
    longest_bridge = 0
    for bridge in bridges:
        strength = 0
        if len(bridge) >= longest_bridge:
            longest_bridge = len(bridge)
            for port_a, port_b in bridge:
                strength += port_a + port_b
            strongest_bridge = max(strongest_bridge, strength)
    return strongest_bridge


if __name__ == '__main__':
    with open('day24.input', 'r') as f:
        INPUT_DATA = f.read()
    print part_one(INPUT_DATA)
    print part_two(INPUT_DATA)
