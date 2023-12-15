import re

data = open("input.txt", "r").read().strip().split("\n")


def part_one(data: list[str]):
    times, distances = [[int(x) for x in re.sub(" +", " ", line.split(":")[1]).strip().split(" ")] for line in data]

    num_ways = 1
    for t, d in zip(times, distances):
        curr_ways = 0

        for i in range(t):
            dist = (t - i) * i
            if dist > d:
                curr_ways += 1
        num_ways *= curr_ways
    return num_ways



def part_two(data: list[str]):
    times, distances = [[int(x) for x in re.sub(" +", "", line.split(":")[1]).strip().split(" ")] for line in data]

    num_ways = 1
    for t, d in zip(times, distances):
        curr_ways = 0

        for i in range(t):
            dist = (t - i) * i
            if dist > d:
                curr_ways += 1
        num_ways *= curr_ways
    return num_ways


print(part_one(data))
print(part_two(data))
