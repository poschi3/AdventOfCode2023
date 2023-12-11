from aocd.models import Puzzle
from collections import Counter
import itertools

puzzle = Puzzle(year=2023, day=11)
input_data = puzzle.examples[0].input_data
input_data = puzzle.input_data

input = input_data.splitlines()

def get_combinations(input):
    galaxies = []
    for y in range(0, len(input)):
        row = input[y]
        for x in range(0, len(row)):
            letter = input[y][x]
            if letter == "#":
                # print(x, y)
                galaxies.append((x, y))

    combinations = list(itertools.combinations(galaxies, 2))
    return combinations

def get_length(combinations, i):
    i -= 1
    sum_a = 0
    for combi in combinations:
        a = combi[0]
        b = combi[1]

        xs = sorted([a[0], b[0]])
        ys = sorted([a[1], b[1]])
        range_x = range(*xs)
        range_y = range(*ys)

        inter_x = zero_x.intersection(range_x)
        inter_y = zero_y.intersection(range_y)

        sum_a += abs(a[0] - b[0]) + abs(a[1] - b[1])
        sum_a += len(inter_x) * i + len(inter_y) * i
    return sum_a

zero_y = set()
zero_x = set()

for y in range(0, len(input)):
    if all(c == "." for c in input[y]):
        zero_y.add(y)

for x in range(0, len(input[0])):
    if all(y[x] == "." for y in input):
        zero_x.add(x)

combinations = get_combinations(input)
sum_a = get_length(combinations, 2)
print(sum_a)
puzzle.answer_a = sum_a

# print(get_length(combinations, 10))
# print(get_length(combinations, 100))

sum_b = get_length(combinations, 1000000)
print(sum_b)
puzzle.answer_b = sum_b
