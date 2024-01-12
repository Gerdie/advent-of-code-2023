FIVE_OF_KIND = 'FIVE OF A KIND'
FOUR_OF_KIND = 'FOUR OF A KIND'
FULL_HOUSE = 'FULL HOUSE'
THREE_OF_KIND = 'THREE OF A KIND'
TWO_PAIR = 'TWO PAIR'
ONE_PAIR = 'ONE PAIR'
HIGH_CARD = 'HIGH CARD'

hand_rankings = {
    HIGH_CARD: 0, 
    ONE_PAIR: 1, 
    TWO_PAIR: 2, 
    THREE_OF_KIND: 3, 
    FULL_HOUSE: 4, 
    FOUR_OF_KIND: 5, 
    FIVE_OF_KIND: 6
}

card_rankings = {
    '2': 0,
    '3': 1,
    '4': 2,
    '5': 3,
    '6': 4,
    '7': 5,
    '8': 6,
    '9': 7,
    'T': 8,
    'J': -1, # switch to 9 for Part 1
    'Q': 10,
    'K': 11,
    'A': 12
    }

class Hand(object):
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
        self.type = self.hand_type(cards)
    
    def __lt__(self, other):
        if self.type == other.type:
            for idx, card in enumerate(self.cards):
                other_card = other.cards[idx]
                if card == other_card:
                    continue
                return card_rankings[card] < card_rankings[other_card]
        return hand_rankings[self.type] < hand_rankings[other.type]
    
    def __repr__(self):
        return '<Hand {} bid {}'.format(self.cards, self.bid)

    @staticmethod
    def hand_type(cards):
        counts = {}
        j_count = 0
        for card in cards:
            if card == 'J':  # rm for Part 1
                j_count += 1
                continue
            counts[card] = counts.get(card, 0) + 1
        if len(counts) == 1 or len(counts) == 0:
            return FIVE_OF_KIND
        if len(counts) == 5:
            return HIGH_CARD
        if len(counts) == 4:
            return ONE_PAIR
        count_values = list(counts.values())
        if j_count:  # rm for Part 1
            max_val = max(count_values)
            for idx, val in enumerate(count_values):
                if val == max_val:
                    count_values[idx] = max_val + j_count
        if len(counts) == 3:
            if 3 in count_values:
                return THREE_OF_KIND
            return TWO_PAIR
        if len(counts) == 2:
            if 4 in count_values:
                return FOUR_OF_KIND
            return FULL_HOUSE

hand_list = []
with open('input.txt') as input_file:
    for line in input_file:
        cards, bid = line.strip().split()
        bid = int(bid)
        hand = Hand(cards, bid)
        hand_list.append(hand)

hand_list.sort()

num_hands = len(hand_list)
total = 0
for idx, hand in enumerate(hand_list):
    score = (idx + 1) * hand.bid
    total += score

print('Total winnings: {}'.format(total))