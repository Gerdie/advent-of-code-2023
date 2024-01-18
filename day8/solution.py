import math
import re

class Node(object):
    def __init__(self, value, left, right):
        self.value = value
        self.right = right
        self.left = left
    
    def __eq__(self, other):
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def __repr__(self):
        return '<Node {}>'.format(self.value)
    
    def set_right(self, right_node):
        self.right = right_node
    
    def set_left(self, left_node):
        self.left = left_node

nodes = {}
directions = None
p = re.compile(r'(?P<node>\w+)\s=\s\((?P<left>\w+),\s(?P<right>\w+)\)')
start_nodes = []

with open('input.txt') as input_file:
    for line in input_file:
        line = line.strip()
        if not line:
            continue
        if not directions:
            directions = line
            continue
        m = p.search(line)
        node_val = m.group('node')
        left = m.group('left')
        right = m.group('right')
        node = Node(node_val, left, right)
        nodes[node_val] = node
        if node_val[-1] == 'A':
            start_nodes.append(node)

def part_one(nodes):
    current_node_value = 'AAA'
    current_node = nodes[current_node_value]
    steps = 0

    while True:
        for direction in directions:
            if direction == 'R':
                current_node_value = current_node.right
            elif direction == 'L':
                current_node_value = current_node.left
            current_node = nodes[current_node_value]
            steps += 1
            
            if current_node_value == 'ZZZ':
                return steps

def find_first_z(node, nodes):
    steps = 0
    while True:
        for direction in directions:
            steps += 1
            if direction == 'R':
                node_value = node.right
            elif direction == 'L':
                node_value = node.left
            if node_value[-1] == 'Z':
                return steps
            node = nodes[node_value]


def part_two(start_nodes, nodes):
    z_at = []
    for node in start_nodes:
        first_z = find_first_z(node, nodes)
        z_at.append(first_z)
    return math.lcm(*z_at)

print('Part One: {}'.format(part_one(nodes)))
print('Part Two: {}'.format(part_two(start_nodes, nodes)))