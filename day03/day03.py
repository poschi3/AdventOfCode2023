from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=3)
#input_data = puzzle.examples[0].input_data
input_data = puzzle.input_data

engine = input_data.splitlines()
max_width = len(engine[0])
max_length = len(engine)
symbols = "*#@+/$&%=-0123456789"

founds = []

def check_around(found, start_x, start_y, symbols):

    x_left = max(start_x - 1, 0)
    x_right = min(start_x + len(found) + 1, max_width)
    y_above = start_y - 1
    y_below = start_y + 1
    around = ""
    if y_above >= 0:
        above = engine[y_above][x_left:x_right]
        around += above

    if y_below < max_length:
        below = engine[y_below][x_left:x_right]
        around += below
    
    if start_x > 0:
        left = engine[start_y][start_x - 1]
        around += left

    if start_x + len(found)  < max_width:
        right = engine[start_y][start_x + len(found)]
        around += right
    res = any(map(around.__contains__, symbols))
    return res

sum = 0  
for y, row in enumerate(engine):

    found_number = None
    found_y = None
    found_x = None
    founds.append([])

    for x, symbol in enumerate(engine[y]):
        if symbol.isnumeric():
            if found_number is None:
                found_number = symbol
                found_y = y
                found_x = x
            else:
                found_number += symbol
        else:
            if found_number is not None:
                
                founds[y].append((found_x, found_x + len(found_number), found_number))
                if check_around(found_number, found_x, found_y, symbols):
                    sum += int(found_number)

                found_number = None
                found_y = None
                found_x = None

    if found_number is not None:
                
        founds[y].append((found_x, found_x + len(found_number), found_number))
        if check_around(found_number, found_x, found_y, symbols):
            sum += int(found_number)

print(sum)
puzzle.answer_a = sum


def find_gears(founds_row, x):
    local_founds = []

    for found in founds_row:
        left = found[0]
        right = found[1]
        if left <= x < right or left <= x-1 < right or left <= x+1 < right:
            local_founds.append(found)
    return local_founds


sum2 = 0
for y, row in enumerate(engine):
    for x, symbol in enumerate(engine[y]):
        if symbol == "*":
            local_founds = []
            if y > 0:
                local_founds.extend(find_gears(founds[y-1], x))
            
            local_founds.extend(find_gears(founds[y], x))

            if y < max_length:
                local_founds.extend(find_gears(founds[y+1], x))
            if(len(local_founds) == 2):
                power = int(local_founds[0][2]) * int(local_founds[1][2])
                sum2 += power
            
print(sum2)
puzzle.answer_b = sum2
