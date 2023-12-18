from aocd.models import Puzzle
from collections import OrderedDict

puzzle = Puzzle(year=2023, day=15)
input_data = puzzle.examples[0].input_data
input_data = puzzle.input_data

def hash(input):
    current_value = 0
    for c in input:
        code = ord(c)
        current_value += code
        current_value *= 17
        current_value = current_value % 256
    return current_value

def part_a():
    sum_a = 0
    for sequence in input_data.split(","):
        sum_a += hash(sequence)

    print(sum_a)
    puzzle.answer_a = sum_a
part_a()

def part_b():
    boxes = dict()
    for sequence in input_data.split(","):
        if sequence[-1] == "-":
            label = sequence[:-1]
            box_no = hash(label)
            box = boxes.setdefault(box_no, OrderedDict())
            if label in box:
                del box[label]
        else:
            label, focal =  sequence.split("=")
            box_no = hash(label)
            box = boxes.setdefault(box_no, OrderedDict())
            box[label] = int(focal)

    sum_b = 0
    for box_no, box in boxes.items():
        l_no = 1
        for focal in box.values():
            this_lense = (box_no+1) * l_no * focal
            sum_b += this_lense
            l_no += 1
    print(sum_b)
    puzzle.answer_b = sum_b

part_b()
