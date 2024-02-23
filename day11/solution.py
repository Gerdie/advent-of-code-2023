EXPAND_BY = 999999

x_idx_to_expand = set()
galaxy = []
with open('input.txt') as input_file:
    for idx, line in enumerate(input_file):
        line = line.strip()
        galaxy.append(line)
        # expand rows
        has_galaxy = False
        for char in line:
            if char == '#':
                has_galaxy = True
                break
        if not has_galaxy:
            x_idx_to_expand.add(idx)

# expand columns
y_idx_to_expand = set()
for y in range(len(galaxy[0])):
    has_galaxy = False
    for row in galaxy:
        if row[y] == '#':
            has_galaxy = True
            break
    if not has_galaxy:
        y_idx_to_expand.add(y)

galaxy_locations = []
for y, row in enumerate(galaxy):
    for x, char in enumerate(row):
        if char == '#':
            galaxy_locations.append((x, y))

def add_galaxy_expansion(max_coord, min_coord, expansion_idxs):
    expand_to = 0
    for coord in range(min_coord, max_coord):
        if coord in expansion_idxs:
            expand_to += EXPAND_BY
    return expand_to



def distance_between(pt1, pt2):
    x1, y1 = pt1
    x2, y2 = pt2
    distance = 0
    if x1 > x2:
        distance += x1 - x2
        distance += add_galaxy_expansion(x1, x2, y_idx_to_expand)
    else:
        distance += x2 - x1
        distance += add_galaxy_expansion(x2, x1, y_idx_to_expand)
    if y1 > y2:
        distance += y1 - y2
        distance += add_galaxy_expansion(y1, y2, x_idx_to_expand)
    else:
        distance += y2 - y1
        distance += add_galaxy_expansion(y2, y1, x_idx_to_expand)
    return distance

distances = []
for idx, loc1 in enumerate(galaxy_locations):
    for loc2 in galaxy_locations[idx+1:]:
        distances.append(distance_between(loc1, loc2))

print('Part One: {}'.format(sum(distances)))