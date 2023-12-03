from functools import reduce
import operator


data = open("input.txt", "r").read().strip().split("\n")

def part_one(data: list[str]):
    res = 0
    max_counts = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    for line in data:
        id, rounds = line.split(":")
        id = int(id.split(" ")[1])
        rounds = [x.strip().split(', ') for x in rounds.strip().split(';')]
        valid = True

        for round in rounds:
            count_valid = lambda x: int(x.split(" ")[0]) <= max_counts[x.split(" ")[1]]
            round_valid = all(map(count_valid, round))
            if not round_valid:
                valid = False

        if valid:
            res += id

    return res

def part_two(data: list[str]):
    res = 0
    for line in data:

        min_counts = {
            "red": 0,
            "green": 0,
            "blue": 0
        }

        id, rounds = line.split(":")
        id = int(id.split(" ")[1])
        rounds = [x.strip().split(', ') for x in rounds.strip().split(';')]

        for round in rounds:
            def parse_cube(cube):
                count, cube_type = cube.split(' ')
                count = int(count)
                min_counts[cube_type] = max(count, min_counts[cube_type])
            list(map(parse_cube, round))

        game_power = reduce(operator.mul, min_counts.values())
        res += game_power

    return res


print(part_one(data))
print(part_two(data))
