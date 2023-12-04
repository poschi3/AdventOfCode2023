from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=4)
input_data = puzzle.examples[0].input_data
#input_data = puzzle.input_data

print(input_data)

for card in input_data.splitlines():
    values = [x.strip() for x in card.split(':')]
    my, winners = [x.strip() for x in values[1].split('|')]
    my2 = [x.strip() for x in my.split(' ')]
    winners2 = [x.strip() for x in winners.split(' ')]

    print(my2)
    print(winners2)


