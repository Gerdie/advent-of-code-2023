def is_symbol(char):
    if char.isdigit():
        return False
    if char.isalpha():
        return False
    if char == '.':
        return False
    return True


with open('input.txt') as file:
    grid = []
    symbol_positions = set()
    gear_adjacent_nums = {}
    total = 0
    y_idx = 0
    # get symbol positions
    for line in file:
        line = line.strip()
        for x_idx, char in enumerate(line):
            if is_symbol(char):
                symbol_positions.add((x_idx, y_idx))
                if char == '*':
                    gear_adjacent_nums[(x_idx, y_idx)] = []
        grid.append(line)
        y_idx += 1
    # get numbers
    for y_idx, row in enumerate(grid):
        num = ''
        valid = False
        adjacent_to = []
        for x_idx, char in enumerate(row):
            if char.isdigit():
                num += char
                if not valid:
                    adjacent_pts = [(x_idx - 1, y_idx), (x_idx + 1, y_idx), (x_idx - 1, y_idx - 1), (x_idx - 1, y_idx + 1), (x_idx + 1, y_idx - 1), (x_idx + 1, y_idx + 1), (x_idx, y_idx - 1), (x_idx, y_idx + 1)]
                    for pt in adjacent_pts:
                        if pt in symbol_positions:
                            valid = True
                            if pt in gear_adjacent_nums:
                                adjacent_to.append(pt)
                # if its the end of the row or the next char isnt a digit
                if x_idx >= len(row) - 1 or not row[x_idx + 1].isdigit():
                    if valid:
                        total += int(num)
                        for gear in adjacent_to:
                            gear_adjacent_nums[gear].append(int(num))
                    num = ''
                    valid = False
                    adjacent_to = []
    # get gears
    total2 = 0
    for gear in gear_adjacent_nums:
        adjacent_nums = gear_adjacent_nums[gear]
        if len(adjacent_nums) == 2:
            total2 += adjacent_nums[0] * adjacent_nums[1]

    print('Part 1: {}'.format(total))
    print('Part 2: {}'.format(total2))
