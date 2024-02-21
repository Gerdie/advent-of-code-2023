maze = []
start_pos = None
with open('input.txt') as input_file:
    for y, line in enumerate(input_file):
        line = line.strip()
        maze.append(line)
        if not start_pos:
            for x, char in enumerate(line):
                if char == 'S':
                    start_pos = (x, y)
                    break

def get_char(position):
    x, y = position
    return maze[y][x]

def get_north(position):
    x, y = position
    return (x, y-1)

def get_south(position):
    x, y = position
    return (x, y+1)

def get_east(position):
    x, y = position
    return (x + 1, y)

def get_west(position):
    x, y = position
    return (x - 1, y)

def first_step(current_pos):
    north_pos = get_north(current_pos)
    south_pos = get_south(current_pos)
    east_pos = get_east(current_pos)
    west_pos = get_west(current_pos)

    north_char = get_char(north_pos)
    if north_char == '|':
        return north_pos
    elif north_char == '7':
        return north_pos
    elif north_char == 'F':
        return north_pos
    
    south_char = get_char(south_pos)
    if south_char == '|':
        return south_pos
    elif south_char == 'L':
        return south_pos
    elif south_char == 'J':
        return south_pos
    
    east_char = get_char(east_pos)
    if east_char == '-':
        return east_pos
    elif east_char == '7':
        return east_pos
    elif east_char == 'J':
        return east_pos
    
    west_char = get_char(west_pos)
    if west_char == '-':
        return west_pos
    elif west_char == 'L':
        return west_pos
    elif west_char == 'F':
        return west_pos

def next_step(current_pos, last_pos):
    north_pos = get_north(current_pos)
    south_pos = get_south(current_pos)
    east_pos = get_east(current_pos)
    west_pos = get_west(current_pos)
    options = []

    char = get_char(current_pos)
    # print('{} at {}'.format(char, current_pos))
    if char == 'S':
        return first_step(current_pos)
    elif char == '|':
        options = [north_pos, south_pos]
    elif char == '-':
        options = [east_pos, west_pos]
    elif char == 'L':
        options = [north_pos, east_pos]
    elif char == 'J':
        options = [north_pos, west_pos]
    elif char == '7':
        options = [south_pos, west_pos]
    elif char == 'F':
        options = [south_pos, east_pos]
    
    options.remove(last_pos)
    return options[0]   

last_pos = None
next_pos = None
current_pos = start_pos
steps = set()
while True:
    steps.add(current_pos)
    next_pos = next_step(current_pos, last_pos)
    if next_pos == start_pos:
        break
    last_pos = current_pos
    current_pos = next_pos

print('Part One: {}'.format(len(steps)/2))

inside_x = set()
for y, row in enumerate(maze):
    is_inside_x = False
    last_char = None
    for x, item in enumerate(row):
        coord = (x, y)
        if coord in steps:
            char = get_char(coord)
            if char == '-':
                continue
            elif char == '|':
                is_inside_x = not is_inside_x
            elif char == 'J' and last_char == 'F':
                pass
            elif char == '7' and last_char == 'L':
                pass
            else:
                is_inside_x = not is_inside_x
            last_char = char
            continue
        if is_inside_x:
            inside_x.add(coord)

print('Part Two: {}'.format(len(inside_x)))
