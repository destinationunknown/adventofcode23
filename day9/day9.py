from collections import deque

data = open("input.txt", "r").read().strip().split("\n")

def parse_data(data: list[str]) -> list[list[int]]:
    return [[int(x) for x in line.split(" ")] for line in data]

def part_one(data: list[str]):
    res = 0
    nums_list = parse_data(data)
    for nums in nums_list:
        stack = deque()
        stack.append(nums)

        while True:
            curr = stack[-1]
            diffs = []
            for i, n in enumerate(curr[:-1]):
                diffs.append(curr[i + 1] - n)

            stack.append(diffs)
            if sum(diffs) == 0:
                break

        while stack:
            curr = stack.pop()

            if stack:
                prev = stack[-1]
                placeholder = prev[-1] + curr[-1]
                prev.append(placeholder)
            else:
                res += curr[-1]

    return res


def part_two(data: list[str]):
    res = 0
    nums_list = parse_data(data)
    for nums in nums_list:
        stack = deque()
        stack.append(nums)

        while True:
            curr = stack[-1]
            diffs = []
            for i, n in enumerate(curr[:-1]):
                diffs.append(curr[i + 1] - n)

            stack.append(diffs)
            if sum(diffs) == 0:
                break

        while stack:
            curr = stack.pop()

            if stack:
                prev = stack[-1]
                placeholder = prev[0] - curr[0]
                prev.insert(0, placeholder)
            else:
                res += curr[0]

    return res


print(part_one(data))
print(part_two(data))
