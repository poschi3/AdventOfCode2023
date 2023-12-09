from aocd.models import Puzzle
from collections import Counter

puzzle = Puzzle(year=2023, day=9)
input_data = puzzle.examples[0].input_data
input_data = puzzle.input_data


def calc_next_row(row):
    last_entry = row[0]
    next_row = []
    for entry in row[1:]:
        next_row.append(entry - last_entry)
        last_entry = entry
    return next_row

def all_zero(row):
    c = Counter(row)
    if 0 not in c:
        return False
    if c[0] < len(row):
        return False
    return True

sum_a = 0
sum_b = 0
for line in input_data.splitlines():
    complete = []
    next_row = [int(x) for x in line.split()]
    complete.append(next_row)

    while not all_zero(next_row):
        next_row = calc_next_row(next_row)
        complete.append(next_row)

    last_entry = 0
    for line in reversed(complete[:-1]):
        last_entry =  line[-1] + last_entry
    sum_a += last_entry

    last_entry = 0
    for line in reversed(complete[:-1]):
        last_entry =  line[0] - last_entry
    sum_b += last_entry

print(sum_a)
puzzle.answer_a = sum_a

print(sum_b)
puzzle.answer_b = sum_b
