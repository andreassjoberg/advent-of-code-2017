#!/usr/bin/env python
"""Day 25 of advent of code"""


from collections import defaultdict
import re


def part_one(data):
    """Part one"""
    write_values = {}
    move_values = {}
    state_values = {}
    states = re.findall(r'In state (\w):', data, re.MULTILINE)
    for state in states:
        reg_zero = re.search(r'In state ' + state + ':[\s\S]*?' +
                             'If the current value is 0:\s+' +
                             '\- Write the value (\d)\.\s+' +
                             '\- Move one slot to the (\w+)\.\s+' +
                             '\- Continue with state (\w)\.', data, re.MULTILINE)
        reg_one = re.search(r'In state ' + state + ':[\s\S]*?' +
                            'If the current value is 1:\s+' +
                            '\- Write the value (\d)\.\s+' +
                            '\- Move one slot to the (\w+)\.\s+' +
                            '\- Continue with state (\w)\.', data, re.MULTILINE)
        write_values[state] = (int(reg_zero.group(1)), int(reg_one.group(1)))
        move_values[state] = (reg_zero.group(2), reg_one.group(2))
        state_values[state] = (reg_zero.group(3), reg_one.group(3))

    current_state = re.search(
        r'^Begin in state (\w)\.', data, re.MULTILINE).group(1)
    num_steps = int(re.search(
        r'Perform a diagnostic checksum after (\d+) steps\.', data, re.MULTILINE).group(1))
    cursor = 0
    tape = {}

    for _ in range(num_steps):
        current_value = 0
        if tape.has_key(cursor) and tape[cursor] == 1:
            current_value = 1
        write_value = write_values[current_state][current_value]
        tape[cursor] = write_value
        if move_values[current_state][current_value] == 'right':
            cursor += 1
        else:
            cursor -= 1
        current_state = state_values[current_state][current_value]
    count = 0
    for value in tape.itervalues():
        if value == 1:
            count += 1
    return count


if __name__ == '__main__':
    with open('day25.input', 'r') as f:
        INPUT_DATA = f.read()
    print part_one(INPUT_DATA)
