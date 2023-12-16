from collections import Counter
from functools import cmp_to_key
import re

data = open("input.txt", "r").read().strip().split("\n")


def get_hand_type(hand: str):
    cnt = Counter(hand)
    max_freq = max(cnt.values())

    if max_freq == 5:
        return 7
    if max_freq == 4:
        return 6
    if max_freq == 3:
        if len(set(hand)) == 2:
            return 5
        else:
            return 4
    if max_freq == 2:
        if len(set(hand)) == 3:
            return 3
        else:
            return 2
    else:
        return 1

def get_hand_type_joker(hand: str):
    cnt = Counter(hand)

    most_common = cnt.most_common(1)[0][0]
    if most_common == "J":
        try:
            most_common = cnt.most_common(2)[1][0]
        except:
            return 7

    hand = re.sub("J", most_common, hand)
    cnt = Counter(hand)

    max_freq = max(cnt.values())

    if max_freq == 5:
        return 7
    if max_freq == 4:
        return 6
    if max_freq == 3:
        if len(set(hand)) == 2:
            return 5
        else:
            return 4
    if max_freq == 2:
        if len(set(hand)) == 3:
            return 3
        else:
            return 2
    else:
        return 1

def hand_comp(a: str, b: str):
    cards = list(reversed("AKQJT98765432"))
    diff = get_hand_type(a) - get_hand_type(b)

    if diff == 0:
        for ac, bc in zip(a, b):
            diffc = cards.index(ac) - cards.index(bc)
            if diffc != 0:
                return diffc
    else:
        return diff

    return 0

def hand_comp_joker(a: str, b: str):
    cards = list(reversed("AKQT98765432J"))
    diff = get_hand_type_joker(a) - get_hand_type_joker(b)

    if diff == 0:
        for ac, bc in zip(a, b):
            diffc = cards.index(ac) - cards.index(bc)
            if diffc != 0:
                return diffc
    else:
        return diff

    return 0

def part_one(data: list[str]):
    hands = [(line.split(" ")[0], int(line.split(" ")[1])) for line in data]
    sorted_hands = list(sorted(hands, key=cmp_to_key(lambda x, y: hand_comp(x[0], y[0]))))

    res = 0
    for index, (hand, bid) in enumerate(sorted_hands):
        res += (index + 1) * bid

    return res

def part_two(data: list[str]):
    hands = [(line.split(" ")[0], int(line.split(" ")[1])) for line in data]
    sorted_hands = list(sorted(hands, key=cmp_to_key(lambda x, y: hand_comp_joker(x[0], y[0]))))

    res = 0
    for index, (hand, bid) in enumerate(sorted_hands):
        res += (index + 1) * bid

    return res

print(part_one(data))
print(part_two(data))
