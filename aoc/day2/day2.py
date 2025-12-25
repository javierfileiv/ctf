import re


def part1(ranges):
    sum = 0
    print(ranges)
    for r in ranges:

    return sum


if __name__ == "__main__":
    ranges = []
    # first parse file to fill in map
    with open("/home/fixp/sourceCode/AOC/day2/input.txt", "r") as file:
        for line in file:
            # skip commented lines
            if line.startswith("#"):
                continue
            ranges = line.strip().split(",")
    part1(ranges)
