from aocd.models import Puzzle
from math import lcm

puzzle = Puzzle(year=2023, day=8)
input_data = puzzle.examples[0].input_data
input_data = puzzle.input_data

splitted_input = input_data.splitlines()
instructions = splitted_input[0]
directions = dict()
starts = []
ends = []

for direction in splitted_input[2:]:
    f, t = direction.split(" = ")
    if f[2] == "A":
        starts.append(f)
    if f[2] == "Z":
        ends.append(f)
    l, r = t[1:-1].split(", ")
    directions[f] = (l, r)

class InstructionsCounter:
    def __init__(self, instructions):
        self.instructions = instructions
        self.i = 0

    def next(self):
        inst = self.instructions[self.i]
        self.i = (self.i+1) % len(self.instructions)
        return inst



class GoGo:
    def __init__(self, directions, start_pos):
        self.directions = directions
        self.start_pos  = start_pos
        self.pos = start_pos
        self.rounds = 0
    
    def go(self, inst):
        self.rounds += 1
        direction = self.directions[self.pos]
        # inst = i_counter.next()
        if inst == "L":
            self.pos = self.directions[self.pos][0]
        else:
            self.pos = self.directions[self.pos][1]
        return self.pos

# A
pos = "AAA"
i_counter = InstructionsCounter(instructions)

go = GoGo(directions, pos)
while pos != "ZZZ":
    inst = i_counter.next()
    pos = go.go(inst)

print(go.rounds)
puzzle.answer_a = go.rounds


# B
# i_counter = InstructionsCounter(instructions)
gos = []
for start in starts:
    go = GoGo(directions, start)
    gos.append(go)

rounds = []
for go in gos:
    pos = None
    i_counter = InstructionsCounter(instructions)
    while pos not in ends:
        inst = i_counter.next()
        pos = go.go(inst)
    rounds.append(go.rounds)

solution_b = lcm(*rounds)
print(solution_b)
puzzle.answer_b = solution_b
