from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=13)
input_data = puzzle.examples[0].input_data
input_data = puzzle.input_data

def is_diff_one_char(a, b):
    found = False
    for i, c_a in enumerate(a):
        if c_a != b[i]:
            if found:
                return False
            found = True
    return found

def check_mirror_vertical(field, y_left):
    y_right = y_left + 1

    while y_left >= 0 and y_right < len(field):
        current_row = field[y_left]
        next_row = field[y_right]
        if current_row != next_row:
            return False
        y_left -= 1
        y_right += 1
    return True

def find_pair_vertical_with_fixing(field):
    pairs = []
    for y in range(0, len(field)-1):
        current_row = field[y]
        next_row = field[y+1]
        if current_row == next_row:
            pairs.append((y, False))
        elif is_diff_one_char(current_row, next_row):
            pairs.append((y, True))
    return pairs

def check_mirror_vertical_with_fixing(field, y_left, fixed):
    y_right = y_left + 1
    y_left -= 1
    y_right += 1

    while y_left >= 0 and y_right < len(field):
        current_row = field[y_left]
        next_row = field[y_right]
        if current_row != next_row:
            if fixed == False and is_diff_one_char(current_row, next_row):
                fixed = True
            elif fixed:
                return False
        y_left -= 1
        y_right += 1
    return fixed

def column(field, x):
    return [row[x] for row in field]

def find_pair_horizontal_with_fixing(field):
    pairs = []
    for x in range(0, len(field[0])-1):
        current_row = column(field, x)
        next_row = column(field, x+1)
        if current_row == next_row:
            pairs.append((x, False))
        elif is_diff_one_char(current_row, next_row):
            pairs.append((x, True))
    return pairs

def check_mirror_horizontal(field, x_top):
    x_bottom = x_top + 1

    while x_top >= 0 and x_bottom < len(field[0]):
        current_row = column(field, x_top)
        next_row = column(field, x_bottom)
        if current_row != next_row:
            return False
        x_top -= 1
        x_bottom += 1
    return True


def check_mirror_horizontal_with_fixing(field, x_top, fixed):
    x_bottom = x_top + 1
    x_top -= 1
    x_bottom += 1

    while x_top >= 0 and x_bottom < len(field[0]):
        current_row = column(field, x_top)
        next_row = column(field, x_bottom)
        if current_row != next_row:
            if fixed == False and is_diff_one_char(current_row, next_row):
                fixed = True
            elif fixed:
                return False
        x_top -= 1
        x_bottom += 1
    return fixed

sum_a = 0
sum_b = 0
patterns = input_data.split("\n\n")
for pattern in patterns:
    field = pattern.splitlines()
    pairs_horizontal = find_pair_vertical_with_fixing(field)
    for y, fixed in pairs_horizontal:
        if not fixed and check_mirror_vertical(field, y):
                sum_a += (y + 1) * 100
        if check_mirror_vertical_with_fixing(field, y, fixed):
            sum_b += (y + 1) * 100

    pairs_vertical = find_pair_horizontal_with_fixing(field)
    for x, fixed in pairs_vertical:
        if not fixed and check_mirror_horizontal(field, x):
            sum_a += x + 1
        if check_mirror_horizontal_with_fixing(field, x, fixed):
            sum_b += x + 1

print(sum_a)
puzzle.answer_a = sum_a

print(sum_b)
puzzle.answer_b = sum_b
