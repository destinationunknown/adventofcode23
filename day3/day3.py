from collections import defaultdict
import regex as re
from itertools import combinations
import operator
from functools import reduce

data = open("input.txt", "r").read().strip().split("\n")

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
directions = {UP, DOWN, LEFT, RIGHT}

def get_coords(data: list[str]):
    num_coords = {}
    symbol_coords = {}
    for row, line in enumerate(data):
        line_split = re.findall(r'\d+|[^.\d]', line)

        symbols = []
        for x in line_split:
            if x.isdigit():
                symbols.append([(x, (row, m.start())) for m in re.finditer(rf"(?<=(^|\D)){x}(?=($|\D))", line)])
            else:
                symbols.append([(x, (row, m.start())) for m in re.finditer(re.escape(x), line)])
        symbols = sum(symbols, [])
        def add_coords(symbol):
            val, coord = symbol
            if val.isdigit():
                num_coords[coord] = int(val)
            elif val != "\n":
                symbol_coords[coord] = val
        list(map(add_coords, symbols))
    return num_coords, symbol_coords

def add_pair(a, b):
    return (a[0] + b[0], a[1] + b[1])

def get_neighbours(num, coord: tuple[int, int]):
    diagonal_dirs = {add_pair(a, b) for (a, b) in combinations(directions, 2)}
    all_directions = directions.union(diagonal_dirs)
    num_digits = len(str(num))
    start_pos = {add_pair(coord, (0, i)) for i in range(num_digits)}
    neighbours = {add_pair(pos, dir) for pos in start_pos for dir in all_directions}
    return neighbours

def part_one(data: list[str]):
    num_coords, symbol_coords = get_coords(data)
    res = 0

    for coord in num_coords:
        num = num_coords[coord]
        if (data[coord[0]][coord[1]] != str(num)[0]):
            print(num, coord)
        n = get_neighbours(num, coord)
        valid_neighbours = list(filter(lambda x: x in symbol_coords, n))
        if len(valid_neighbours):
            res += num

    return res

def part_two(data: list[str]):
    num_coords, symbol_coords = get_coords(data)
    res = 0

    gears = defaultdict(list)

    for coord in num_coords:
        num = num_coords[coord]
        if (data[coord[0]][coord[1]] != str(num)[0]):
            print(num, coord)
        n = get_neighbours(num, coord)
        valid_neighbours = list(filter(lambda x: x in symbol_coords, n))
        for neighbour in valid_neighbours:
            if symbol_coords[neighbour] == "*":
                gears[neighbour].append(num)

    for gear in gears:
        if len(gears[gear]) == 2:
            res += reduce(operator.mul, gears[gear])

    return res


print(part_one(data))
print(part_two(data))
