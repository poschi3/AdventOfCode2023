from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=1)
input_data = puzzle.input_data

matches_a = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}

matches_b = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def get_num(matches, method, min):
    pos = None
    best_value = None
    for key, value in matches.items():
        found_pos = method(key)
        if min:
            if found_pos >= 0 and (pos is None or found_pos < pos):
                pos = found_pos
                best_value = value
        else: # max
            if found_pos >= 0 and (pos is None or found_pos > pos):
                pos = found_pos
                best_value = value

    return best_value


def solve_a():
    sum = 0
    for calibration in input_data.splitlines():
        a = get_num(matches_a, calibration.find, True)
        b = get_num(matches_a, calibration.rfind, False)
        sum += a*10 + b
    print(sum)


def solve_b():
    sum = 0
    for calibration in input_data.splitlines():
        a = get_num(matches_b, calibration.find, True)
        b = get_num(matches_b, calibration.rfind, False)
        sum += a*10 + b
    print(sum)

solve_a()
solve_b()
