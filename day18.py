#!/usr/bin/env python
"""Day 18 of advent of code"""


def get_value(values, register):
    """Gets the value"""
    if register >= 'a' and register <= 'z':
        return values[register]
    return int(register)


def part_one(data):
    """Part one"""
    values = {}
    sounds_played = []
    lines = data.splitlines()
    for line in lines:
        values[line.split(' ')[1]] = 0
    i = 0
    while i < len(lines):
        split = lines[i].split(' ')
        if split[0] == 'snd':
            sounds_played.append(values[split[1]])
        elif split[0] == 'set':
            values[split[1]] = get_value(values, split[2])
        elif split[0] == 'add':
            values[split[1]] = values[split[1]] + get_value(values, split[2])
        elif split[0] == 'mul':
            values[split[1]] = values[split[1]] * get_value(values, split[2])
        elif split[0] == 'mod':
            values[split[1]] = values[split[1]] % get_value(values, split[2])
        elif split[0] == 'rcv':
            if sounds_played[-1] > 0:
                return sounds_played[-1]
        elif split[0] == 'jgz' and values[split[1]] > 0:
            i += get_value(values, split[2])
            continue
        i += 1


def run_forrest(instructions, values, queue_read, queue_write, i):
    """Runs"""
    sends = 0
    has_moved = False
    while i < len(instructions):
        split = instructions[i].split(' ')
        if split[0] == 'snd':
            sends += 1
            queue_write.append(get_value(values, split[1]))
        elif split[0] == 'set':
            values[split[1]] = get_value(values, split[2])
        elif split[0] == 'add':
            values[split[1]] = values[split[1]] + get_value(values, split[2])
        elif split[0] == 'mul':
            values[split[1]] = values[split[1]] * get_value(values, split[2])
        elif split[0] == 'mod':
            values[split[1]] = values[split[1]] % get_value(values, split[2])
        elif split[0] == 'rcv':
            if queue_read:
                values[split[1]] = queue_read[0]
                del queue_read[0]
            else:
                break
        elif split[0] == 'jgz' and get_value(values, split[1]) > 0:
            has_moved = True
            i += get_value(values, split[2])
            continue
        has_moved = True
        i += 1
    return (i, sends, has_moved)


def part_two(data):
    """Part two"""
    program_zero = {}
    program_one = {}
    queue_zero = []
    queue_one = []
    instructions = data.splitlines()
    for line in instructions:
        register = line.split(' ')[1]
        if register >= 'a' and register <= 'z':
            program_zero[register] = 0
            program_one[register] = 0
    program_one['p'] = 1
    i_zero = i_one = total_sends_one = 0
    has_moved = True
    while has_moved:
        i_zero, _, zero_moved = run_forrest(instructions, program_zero,
                                            queue_zero, queue_one, i_zero)
        i_one, sends_one, one_moved = run_forrest(instructions, program_one,
                                                  queue_one, queue_zero, i_one)
        total_sends_one += sends_one
        has_moved = zero_moved or one_moved
    return total_sends_one


if __name__ == '__main__':
    with open('day18.input', 'r') as f:
        INPUT_DATA = f.read()
    print part_one(INPUT_DATA)
    print part_two(INPUT_DATA)
