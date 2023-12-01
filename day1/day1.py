data = open("input.txt", "r").read().strip().split("\n")

def part_one(data: list[str]):
    res = 0
    for line in data:
        print(line)
        digits = [int(x) for x in line if x.isdigit()]
        res += (digits[0] * 10) + digits[-1]
    return res


def part_two(data: list[str]):
    digit_names = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    res = 0

    for line in data:
        digits = [(i,int(x)) for i, x in enumerate(line) if x.isdigit()]
        digits += [(line.find(digit_name), digit_names[digit_name]) for digit_name in digit_names if line.find(digit_name) != -1]
        digits += [(line.rfind(digit_name), digit_names[digit_name]) for digit_name in digit_names if line.find(digit_name) != -1]
        digits.sort(key=lambda x: x[0])
        res += (digits[0][1] * 10) + digits[-1][1]

    return res


print(part_one(data))
print(part_two(data))
