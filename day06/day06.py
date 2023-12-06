from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=6)
input_data = puzzle.examples[0].input_data
input_data = puzzle.input_data

input = input_data.splitlines()

time = [int(x) for x in input[0].split()[1:]]
distance = [int(x) for x in input[1].split()[1:]]

def calc(t, d):
    working_sum = 0

    for j in range(1, t):
        m = j * (t-j)
        if m > d:
            working_sum += 1

    return working_sum


working_mult = 1
for i in range(0, len(time)):
    working_sum = 0
    t = time[i]
    d = distance[i]
    working_mult *= calc(t, d)

print(working_mult)
puzzle.answer_a = working_mult

time_b = int(input[0].split(maxsplit=1)[1].replace(" ", ""))
distance_b = int(input[1].split(maxsplit=1)[1].replace(" ", ""))

part_b = calc(time_b, distance_b)
print(part_b)

puzzle.answer_b = part_b
