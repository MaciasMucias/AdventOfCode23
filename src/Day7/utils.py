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


def extract_jokers(hand: Hand):
    if "J" not in hand.cards:
        return 0
    if len(hand.cards) == 1:
        return 0
    return hand.cards.pop("J")


def add_jokers_back(hand, jokers):
    if jokers == 0:
        return
    hand.cards["J"] = jokers


def compare_hands_with_jokers(hand1: Hand, hand2: Hand):
    hand1_jokers = extract_jokers(hand1)
    hand2_jokers = extract_jokers(hand2)

    card_amounts1 = sorted(hand1.cards.values(), reverse=True)
    card_amounts2 = sorted(hand2.cards.values(), reverse=True)

    add_jokers_back(hand1, hand1_jokers)
    add_jokers_back(hand2, hand2_jokers)

    card_amounts1[0] += hand1_jokers
    card_amounts2[0] += hand2_jokers

    for card_1, card2 in zip(card_amounts1, card_amounts2):
        if card_1 > card2:
            return 1
        elif card2 > card_1:
            return -1
    cmp_rep1 = hand1.raw_hand.replace("A", "Z").replace("K", "Y").replace("Q", "X").replace("J", "0").replace("T", "V")
    cmp_rep2 = hand2.raw_hand.replace("A", "Z").replace("K", "Y").replace("Q", "X").replace("J", "0").replace("T", "V")
    return (cmp_rep1 > cmp_rep2) - (cmp_rep1 < cmp_rep2)


def parse_hands_from_input(path):
    lines = load_input(path)
    hands = [parse_hand_from_line(line) for line in lines]
    return hands
