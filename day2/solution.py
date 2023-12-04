def parse_line(line):
    # Game 1: 2 red, 2 green; 6 red, 3 green; 2 red, 1 green, 2 blue; 1 red
    line = line.strip()
    game, rounds = line.split(':')
    game_num = int(game.split(' ')[-1])
    for round in rounds.strip().split(';'):
        for marbles in round.strip().split(','):
            num, color = marbles.strip().split(' ')
            num = int(num)
            if color == 'red' and num > 12:
                return 0
            if color == 'green' and num > 13:
                return 0
            if color == 'blue' and num > 14:
                return 0
    return game_num

def parse_line2(line):
    line = line.strip()
    _, rounds = line.split(':')
    max_red = 0
    max_green = 0
    max_blue = 0
    for round in rounds.strip().split(';'):
        for marbles in round.strip().split(','):
            num, color = marbles.strip().split(' ')
            num = int(num)
            if color == 'red' and num > max_red:
                max_red = num
            if color == 'green' and num > max_green:
                max_green = num
            if color == 'blue' and num > max_blue:
                max_blue = num
    return max_red * max_green * max_blue


with open('input.txt') as file:
    total = 0
    total2 = 0
    for line in file:
        total += parse_line(line)
        total2 += parse_line2(line)
    print('Part 1: {}'.format(total))
    print('Part 2: {}'.format(total2))
