def is_possible(springs, grouping):
    if len(springs) < grouping:
        return False
    if len(springs) > grouping:
        if springs[-grouping -1] == '#':
            return False
    sub_springs = springs[-grouping:]
    for char in sub_springs[:-1]:
        if char == '.':
            return False
    return True


def count_arrangements(springs, spring_groupings):
    # zero conditions
    if not springs and not spring_groupings:
        return 1
    if not spring_groupings:
        for char in springs:
            if char == '#':
                return 0
        return 1
    if not springs:
        return 0
    # prune
    if springs[-1] == '.':
        return count_arrangements(springs[:-1], spring_groupings)
    # account for broken spring
    if springs[-1] == '#':
        grp = spring_groupings[-1]
        if is_possible(springs, grp):
            return count_arrangements(springs[:-grp - 1], spring_groupings[:-1])
        return 0
    # account for unknown spring
    if springs[-1] == '?':
        springs = springs[:-1]
        return count_arrangements(springs + '#', spring_groupings) + count_arrangements(springs + '.', spring_groupings)


total_arrangements = 0
with open('input.txt') as input_file:
    for line in input_file:
        line = line.strip()
        springs, spring_groupings = line.split()
        spring_groupings = list(map(int, spring_groupings.split(',')))
        arrangements = count_arrangements(springs, spring_groupings)
        total_arrangements += arrangements

print('Part One: {}'.format(total_arrangements))