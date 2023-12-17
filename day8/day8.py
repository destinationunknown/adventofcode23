import re

data = open("input.txt", "r").read().strip().split("\n")

def parse_input(data: list[str]):
    inst = data[0]

    map = {}
    for line in data[2:]:
        start = line.split("=")[0].strip()
        l = re.findall(r"(?<=\()[A-Z]+(?=,)", line)[0]
        r = re.findall(r"(?<= )[A-Z]+(?=\))", line)[0]
        map[start] = (l, r)

    return inst, map


inst_to_index = {
    "L": 0,
    "R": 1
}

def part_one(data: list[str]):

    inst, map = parse_input(data)

    curr = "AAA"
    inst_index = 0
    steps = 0

    while curr != "ZZZ":
        curr_inst = inst[inst_index]
        inst_index = (inst_index + 1) % len(inst)

        curr = map[curr][inst_to_index[curr_inst]]
        steps += 1

    return steps



def part_two(data: list[str]):
    ...

print(part_one(data))
print(part_two(data))
