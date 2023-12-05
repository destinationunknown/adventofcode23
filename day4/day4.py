from collections import defaultdict
import re

data = open("input.txt", "r").read().strip().split("\n")

def part_one(data: list[str]):
    res = 0
    for line in data:
        _, nums = line.split(":")
        winning, player = [{int(x) for x in re.sub(" +", " ", y.strip()).split(" ")} for y in nums.split("|")]
        num_winning = len(winning.intersection(player))
        if num_winning:
            res += pow(2, num_winning - 1)

    return res

def part_two(data: list[str]):
    card_copies = defaultdict(int)
    for i, line in enumerate(data):
        _, nums = line.split(":")
        winning, player = [{int(x) for x in re.sub(" +", " ", y.strip()).split(" ")} for y in nums.split("|")]
        num_winning = len(winning.intersection(player))
        card_copies[i] += 1
        if num_winning:
            for j in range(i + 1, i + 1 + num_winning):
                card_copies[j] += card_copies[i]

    res = sum(card_copies.values())
    return res

print(part_one(data))
print(part_two(data))
