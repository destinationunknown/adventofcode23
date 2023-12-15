import regex as re
import itertools

data = open("input.txt", "r").read().strip().split("\n")

order = {
    "seed": "soil",
    "soil": "fertilizer",
    "fertilizer": "water",
    "water": "light",
    "light": "temperature",
    "temperature": "humidity",
    "humidity": "location",
}

def parse_input(data: list[str]):
    seeds = [int(x) for x in data[0].split(":")[1].strip().split(" ")]
    map_descs = [list(group) for key, group in itertools.groupby(data[1:], lambda x: x == "") if not key]

    maps = {}

    for desc in map_descs:
        name, vals = desc[0], desc[1:]
        src_name = re.findall(r"(?<=^)[a-z]+(?=-)", name)[0]
        dst_name = re.findall(r"(?<=-)[a-z]+(?= )", name)[0]

        curr_map = {}

        for val in vals:
            dst_start, src_start, range_size = [int(x) for x in val.split(" ")]
            offset = dst_start - src_start
            curr_map[(src_start, src_start + range_size)] = offset

        maps[(src_name, dst_name)] = curr_map

    return seeds, maps

def part_one(data: list[str]):
    seeds, maps = parse_input(data)

    min_location = float("inf")
    for seed in seeds:
        curr_val = seed
        src = "seed"

        while src in order:
            dst = order[src]
            m = maps[(src, dst)]
            for rng in m:
                if curr_val in range(rng[0], rng[1] + 1):
                    curr_val += m[rng]
                    break

            src = dst
        min_location = min(min_location, curr_val)
    return min_location


def part_two(data: list[str]):
    raw_seeds, maps = parse_input(data)
    seeds = []

    # transform raw seeds into ranges with start and ends
    for i in range(0, len(raw_seeds), 2):
        seeds.append((raw_seeds[i], raw_seeds[i] + raw_seeds[i + 1]))


    src = "seed"
    while src in order:
        dst = order[src]
        m = maps[(src, dst)]

        next_seeds = []
        while seeds:
            ss, se = seeds.pop()

            # check all the map ranges against the current seed range
            for ms, me in m:

                # find the overlap between the ranges
                os = max(ss, ms)
                oe = min(se, me)

                # check if the overlap is valid
                if os < oe:
                    ns = os + m[ms, me]
                    ne = oe + m[ms, me]
                    next_seeds.append((ns, ne))

                    # reconsider the parts of the seed range that were not overlapping
                    if ss < os:
                        seeds.append((ss, os))
                    if oe < se:
                        seeds.append((oe, se))
                    break
            else:
                # if none of the ranges match, the seed range is untransformed
                next_seeds.append((ss, se))


        seeds = next_seeds
        src = dst

    return sorted(seeds)[0][0]



print(part_one(data))
print(part_two(data))
