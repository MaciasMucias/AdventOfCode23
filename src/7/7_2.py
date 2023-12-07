from functools import cmp_to_key
from utils import parse_hands_from_input, compare_hands_with_jokers


hands = parse_hands_from_input("../../Inputs/7")

sorted_hands = sorted(hands, key=cmp_to_key(compare_hands_with_jokers))

winnings = 0
for ind, hand in enumerate(sorted_hands, 1):
    winnings += hand.bid * ind

print(winnings)
