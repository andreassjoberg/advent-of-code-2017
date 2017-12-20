#!/usr/bin/env python
"""Day 20 of advent of code"""

from collections import defaultdict


def read(part):
    """Reads input"""
    part = part[3:].replace('>', '')
    return map(int, part.split(','))


def increase_velocity(particle):
    """Increase velocity"""
    particle[1][0] = particle[1][0] + particle[2][0]
    particle[1][1] = particle[1][1] + particle[2][1]
    particle[1][2] = particle[1][2] + particle[2][2]


def increase_position(particle):
    """Increase position"""
    particle[0][0] = particle[0][0] + particle[1][0]
    particle[0][1] = particle[0][1] + particle[1][1]
    particle[0][2] = particle[0][2] + particle[1][2]


def move_particle(particle, iterations):
    """Moves the particle"""
    for _ in range(iterations):
        increase_velocity(particle)
        increase_position(particle)


def get_distance(particle):
    """Gets the Manhattan distance"""
    return abs(particle[0][0]) + abs(particle[0][1]) + abs(particle[0][2])


def part_one(data):
    """Part one"""
    particles = []
    i = 0
    for line in data.splitlines():
        split = line.split('>, ')
        p, v, a = read(split[0]), read(split[1]), read(split[2])
        particles.append([p, v, a, i])
        i += 1
    for particle in particles:
        move_particle(particle, 1000)
    closest_particle = [particles[0][3], get_distance(particles[0])]
    for particle in particles:
        distance = get_distance(particle)
        if distance < closest_particle[1]:
            closest_particle = [particle[3], distance]
    return closest_particle[0]


def part_two(data):
    """Part two"""
    particles = []
    i = 0
    for line in data.splitlines():
        split = line.split('>, ')
        p, v, a = read(split[0]), read(split[1]), read(split[2])
        particles.append([p, v, a, i])
        i += 1
    for _ in range(1000):
        for particle in particles:
            move_particle(particle, 1)
        taken = defaultdict(list)
        for particle in particles:
            taken[tuple([particle[0][0], particle[0][1],
                         particle[0][2]])].append(particle[3])
        for value in taken.itervalues():
            if len(value) > 1:
                for i in value:
                    particles = [
                        particle for particle in particles if particle[3] != i]
    return len(particles)


if __name__ == '__main__':
    with open('day20.input', 'r') as f:
        INPUT_DATA = f.read()
    print part_one(INPUT_DATA)
    print part_two(INPUT_DATA)
