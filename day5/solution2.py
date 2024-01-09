
class Node(object):
    def __init__(self, metric_name, metric_min, metric_max):
        self.metric_name = metric_name
        self.metric_min = metric_min
        self.metric_max = metric_max
        self.new_metric_max = None
        self.new_metric_min = None
        self.children = []
        self.parent = None
    
    def __eq__(self, other):
        return (
            self.metric_name == other.metric_name and 
            self.metric_min == other.metric_min and
            self.metric_max == other.metric_max
            )

    def __hash__(self):
        return hash('{}:{}-{}'.format(self.metric_name, self.metric_min, self.metric_max))

    def __repr__(self):
        self_str = '<{} {}-{}>'.format(self.metric_name, self.metric_min, self.metric_max)
        for child in self.children:
            self_str += ' ' + child.__repr__()
        return self_str

    def resolve(self):
        if self.new_metric_max:
            self.metric_max = self.new_metric_max
            self.new_metric_max = None
        if self.new_metric_min:
            self.metric_min = self.new_metric_min
            self.new_metric_min = None
        for child in self.children:
            child.resolve()

class Tree(object):
    def __init__(self):
        self.seeds = []
    
    def __repr__(self):
        self_str = '<Tree>\n'
        for seed in self.seeds:
            self_str += ' ' + seed.__repr__() + '\n'
        return self_str
    
    @staticmethod
    def add_node(parent, metric_name, metric_min, metric_max):
        node = Node(metric_name, metric_min, metric_max)
        if parent:
            parent.children.append(node)
            node.parent = parent
        return node
    
    def add_seed(self, seed_min, seed_max):
        seed_node = self.add_node(None, 'seed', seed_min, seed_max)
        self.seeds.append(seed_node)
        return seed_node
    
    def split_node(self, node, split_point, direction, children=None):
        if direction == 'up':
            new_node = Node(node.metric_name, split_point + 1, node.metric_max)
            new_node.children = children or []

            node.new_metric_max = split_point
        
        if direction == 'down':
            new_node = Node(node.metric_name, node.metric_min, split_point - 1)
            new_node.children = children or []

            node.new_metric_min = split_point

        if node.parent:
            offset = node.metric_max - split_point
            new_parent = self.split_node(
                node.parent,
                node.parent.metric_max - offset,
                direction,
                children=[new_node])
            new_node.parent = new_parent
        
        if node.metric_name == 'seed':
            self.seeds.append(new_node)

        return new_node
    
    def resolve(self):
        for seed in self.seeds:
            seed.resolve()

class TreeBuilder(object):
    def __init__(self):
        self.tree = Tree()
        self.current_metric = 'seed'
        self.looking_for = set()
        self.found = set()
    
    def parse_seeds(self, line):
        line = line.strip('seeds: ')
        seed_list = map(int, line.split())
        seed_start = None
        for num in seed_list:
            if seed_start is None:
                seed_start = num
                continue
            seed = self.tree.add_seed(seed_start, seed_start + num - 1)
            self.found.add(seed)
            # reset
            seed_start = None
        return self.found
    
    def finish_metric(self):
        for remaining in self.looking_for:
            new = self.tree.add_node(remaining,
                                     self.current_metric,
                                     remaining.metric_min,
                                     remaining.metric_max)
            self.found.add(new)
        self.looking_for = self.found
        self.found = set()
        print(self.tree)
    
    def add_metric(self, line):
        self.finish_metric()
        self.current_metric = line[:-5].split('-to-')[1]
    
    def parse_metric(self, line):
        if not self.looking_for:
            return
        
        line = list(map(int, line.split()))
        dest_start, source_start, ranges = line

        nodes_to_add = []
        nodes_to_rm = []
        need_resolve = False
        for node in self.looking_for:
            # 1. min is above given range
            if node.metric_min >= source_start + ranges:
                continue
            # 2. max is below given range
            if node.metric_max < source_start:
                continue
            # 3. there's some intersection of the ranges
            offset = node.metric_min - source_start
            metric_min = dest_start + offset
            metric_max = metric_min + (node.metric_max - node.metric_min)
            # A. the node is higher than the new range
            if node.metric_max >= source_start + ranges:
                # chop off the top
                new_node = self.tree.split_node(node, source_start + ranges - 1, 'up')
                nodes_to_add.append(new_node)
                need_resolve = True

                metric_min = dest_start + offset
                metric_max = metric_min + (node.new_metric_max - node.metric_min)
            # B. the node is lower than the new range
            if node.metric_min < source_start:
                # chop off the bottom
                new_node = self.tree.split_node(node, source_start, 'down')
                nodes_to_add.append(new_node)
                need_resolve = True

                offset = node.new_metric_min - source_start
                metric_min = dest_start + offset
                metric_max = metric_min + (node.new_metric_max or node.metric_max) - node.new_metric_min
            child_node = self.tree.add_node(
                node, 
                self.current_metric,
                metric_min,
                metric_max)
            self.found.add(child_node)
            nodes_to_rm.append(node)
                    
        for rm_node in nodes_to_rm:
            self.looking_for.remove(rm_node)
        for ad_node in nodes_to_add:
            self.looking_for.add(ad_node)
        if need_resolve:
            self.tree.resolve()

tree_builder = TreeBuilder()
with open('input.txt') as input_file:
    for line in input_file:
        line = line.strip()
        if not line:
            continue
        if line.startswith('seeds:'):
            tree_builder.parse_seeds(line)
            continue
        if line.endswith('map:'):
            tree_builder.add_metric(line)
            continue
        tree_builder.parse_metric(line)
    tree_builder.finish_metric()


lowest_location = None
for node in tree_builder.looking_for:
    if lowest_location is None:
        lowest_location = node.metric_min
        continue
    if node.metric_min < lowest_location:
        lowest_location = node.metric_min


print('Lowest location: {}'.format(lowest_location))