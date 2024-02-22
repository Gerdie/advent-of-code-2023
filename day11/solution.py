
galaxy = []
with open('input.txt') as input_file:
    for line in input_file:
        line = line.strip()
        galaxy.append(line)
        # expand rows
        has_galaxy = False
        for char in line:
            if char == '#':
                has_galaxy = True
                break
        if not has_galaxy:
            galaxy.append(line)

# expand columns
y_idx_to_expand = []
for y in range(len(galaxy[0])):
    has_galaxy = False
    for row in galaxy:
        if row[y] == '#':
            has_galaxy = True
            break
    if not has_galaxy:
        y_idx_to_expand.append(y)

while y_idx_to_expand:
    y = y_idx_to_expand.pop()
    for idx in range(len(galaxy)):
        row = galaxy[idx]
        row = row[0:y] + '.' + row[y:]
        galaxy[idx] = row

galaxy_locations = []
for y, row in enumerate(galaxy):
    for x, char in enumerate(row):
        if char == '#':
            galaxy_locations.append((x, y))

def distance_between(pt1, pt2):
    x1, y1 = pt1
    x2, y2 = pt2
    distance = 0
    if x1 > x2:
        distance += x1 - x2
    else:
        distance += x2 - x1
    if y1 > y2:
        distance += y1 - y2
    else:
        distance += y2 - y1
    return distance

distances = []
for idx, loc1 in enumerate(galaxy_locations):
    for loc2 in galaxy_locations[idx:]:
        distances.append(distance_between(loc1, loc2))

print('Part One: {}'.format(sum(distances)))