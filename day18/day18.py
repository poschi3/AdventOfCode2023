from aocd.models import Puzzle
import sys

puzzle = Puzzle(year=2023, day=18)
input_data = puzzle.examples[0].input_data
input_data = puzzle.input_data

directions_a = {
    "U": ( 0, -1),
    "D": ( 0, +1),
    "R": (+1,  0),
    "L": (-1,  0),
}

directions_b = {
    "3": ( 0, -1), # U
    "1": ( 0, +1), # D
    "0": (+1,  0), # R
    "2": (-1,  0), # L
}

def comb(a, b, fakt = 1):
    return (a[0] + (b[0] * fakt), a[1] + (b[1] * fakt))

def extract_a(row):
    direction, num, color = row.split()
    num = int(num)
    direction = directions_a[direction]
    return direction, num

def extract_b(row):
    direction, num, color = row.split()
    direction = color[-2]
    direction = directions_b[direction]
    num = int(color[2:-2], 16)
    return direction, num


def get_vectors(input_data, extractor):
    pos = (0, 0)
    all_pos = [pos]

    for row in input_data.splitlines():
        direction, num = extractor(row)
        new_pos = comb(pos, direction, num)
        all_pos.append(new_pos)
        pos = new_pos
    return all_pos

def area(p):
    border = 2
    s = 0.0
    for ((x0, y0), (x1, y1)) in segments(p):
        s += x0*y1 - x1*y0
        border += abs(x0 - x1) + abs(y0 - y1)
    a = abs(s)
    return 0.5 * (a + border)

def segments(p):
    return zip(p, p[1:] + [p[0]])


def input_a(input_data):
    all = get_vectors(input_data, extract_a)
    a = area(all)
    return int(a)

sum_a = input_a(input_data)
print(sum_a)
puzzle.answer_a = sum_a

def input_b(input_data):
    all = get_vectors(input_data, extract_b)
    a = area(all)
    return int(a)

sum_b = input_b(input_data)
print(sum_b)
puzzle.answer_b = sum_b
