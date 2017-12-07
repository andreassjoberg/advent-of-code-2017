#!/usr/bin/env python
"""Day 07 of advent of code"""


def read_nodes(data):
    """Reads the input data as nodes"""
    nodes = []
    for line in data.splitlines():
        words = line.split(" -> ")
        first_index = words[0].index("(") + 1
        second_index = words[0].index(")")
        children = None
        if len(words) > 1:  # Has children
            children = words[1].split(", ")
        nodes.append((words[0][:first_index - 2],
                      int(words[0][first_index:second_index]), children))
    return nodes


def get_node(node_name, nodes):
    """Gets the index of the node"""
    for i in range(0, len(nodes)):
        if nodes[i][0] == node_name:
            return nodes[i]


def child_weight(child, nodes):
    """Gets the child weight"""
    if child[2] is None:
        return child[1]
    weight = 0
    for sub_child in child[2]:
        weight += child_weight(get_node(sub_child, nodes), nodes)
    return weight + child[1]


def get_common_weight(weights):
    """Gets the common weight"""
    for weight in weights:
        if weights.count(weight) > 1:
            return weight
    return None


def check_balanced(node, nodes, common_weight, last_off_weight):
    """Checks if children are unbalanced with parent"""
    weight = node[1]
    children = node[2]
    if children is not None:
        weights = []
        for child in children:
            child_node = get_node(child, nodes)
            child_node_weight = child_weight(child_node, nodes)
            weights.append(child_node_weight)
        for i in range(0, len(weights)):
            if weights.count(weights[i]) == 1:
                common_weight = get_common_weight(weights)
                last_off_weight = weights[i]
                return check_balanced(get_node(children[i], nodes), nodes,
                                      common_weight, last_off_weight)
    return weight - (last_off_weight - common_weight)


def part_one(data):
    """Part one"""
    nodes = read_nodes(data)
    for name, _, _ in nodes:
        count = data.count(name)
        if count == 1:
            return name
    return None


def part_two(root_node_name, data):
    """Part two"""
    nodes = read_nodes(data)
    root_node = get_node(root_node_name, nodes)
    return check_balanced(root_node, nodes, 0, 0)


if __name__ == '__main__':
    with open('day07.input', 'r') as f:
        INPUT_DATA = f.read()
    PART_ONE_ANSWER = part_one(INPUT_DATA)
    print PART_ONE_ANSWER
    print part_two(PART_ONE_ANSWER, INPUT_DATA)
