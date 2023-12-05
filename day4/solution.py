def parse_line(line):
    # Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    _, nums = line.strip().split(':')
    winning, drawn = nums.strip().split('|')
    winning = set(winning.split())
    drawn = drawn.split()
    pts = 0
    for num in drawn:
        if num not in winning:
            continue
        if pts == 0:
            pts = 1
        else:
            pts = pts * 2
    return pts

def parse_line2(line):
    # Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    card, nums = line.strip().split(':')
    card_num = int(card.split()[-1])
    winning, drawn = nums.strip().split('|')
    winning = set(winning.split())
    drawn = drawn.split()
    matches = 0
    for num in drawn:
        if num in winning:
            matches += 1

    return card_num, [card_num + num + 1 for num in range(matches)]



with open('input.txt') as file:
    card_to_winnings = {}
    total = 0
    for line in file:
        total += parse_line(line)
        card_num, winnings = parse_line2(line)
        card_to_winnings[card_num] = winnings
    
    total_cards = 0
    for card in card_to_winnings:
        total_cards += 1
        copies = card_to_winnings[card]
        while copies:
            copy = copies.pop()
            total_cards += 1
            copies.extend(card_to_winnings[copy])


    print('Part 1: {}'.format(total))
    print('Part 2: {}'.format(total_cards))
