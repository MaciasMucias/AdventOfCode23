from src.utils import load_input
from collections import Counter
from dataclasses import dataclass


@dataclass
class Hand:
    cards: Counter
    bid: int
    raw_hand: str


def parse_hand_from_line(line: str) -> Hand:
    hand, bid = line.split()
    return Hand(cards=Counter(hand), bid=int(bid), raw_hand=hand)


def compare_hands(hand1: Hand, hand2: Hand):
    card_amounts1 = sorted(hand1.cards.values(), reverse=True)
    card_amounts2 = sorted(hand2.cards.values(), reverse=True)

    for card_1, card2 in zip(card_amounts1, card_amounts2):
        if card_1 > card2:
            return 1
        elif card2 > card_1:
            return -1
    cmp_rep1 = hand1.raw_hand.replace("A", "Z").replace("K", "Y").replace("Q", "X").replace("J", "W").replace("T", "V")
    cmp_rep2 = hand2.raw_hand.replace("A", "Z").replace("K", "Y").replace("Q", "X").replace("J", "W").replace("T", "V")
    return (cmp_rep1 > cmp_rep2) - (cmp_rep1 < cmp_rep2)  # from locale.strcoll


def parse_hands_from_input(path):
    lines = load_input(path)
    hands = [parse_hand_from_line(line) for line in lines]
    return hands
