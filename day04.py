#!/usr/bin/env python
"""Day 04 of advent of code"""


def part_one(data):
    """Part one"""
    valid = 0
    for row in data.splitlines():
        words = sorted(row.split())
        is_valid = True
        for i in range(1, len(words)):
            if words[i - 1] == words[i]:
                is_valid = False
                break
        if is_valid:
            valid += 1
    return valid

# Part two


def is_anagram(word_a, word_b):
    """Checks if two words are anagrams to each other"""
    if len(word_a) != len(word_b):
        return False
    word_a = sorted(list(word_a))
    word_b = sorted(list(word_b))
    for k in range(0, len(word_a)):
        if word_a[k] != word_b[k]:
            return False
    return True


def part_two(data):
    """Part two"""
    valid = 0
    for row in data.splitlines():
        words = sorted(row.split())
        is_valid = True
        for i in range(1, len(words)):
            if words[i - 1] == words[i]:
                is_valid = False
                break
        for i in range(0, len(words)):
            for j in range(i + 1, len(words)):
                if is_anagram(words[i], words[j]):
                    is_valid = False
                    break
            if not is_valid:
                break
        if is_valid:
            valid += 1
    return valid


if __name__ == '__main__':
    with open('day04.input', 'r') as f:
        INPUT_DATA = f.read()
    print part_one(INPUT_DATA)
    print part_two(INPUT_DATA)
