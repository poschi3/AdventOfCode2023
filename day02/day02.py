from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=2)
#input_data = puzzle.examples[0].input_data
input_data = puzzle.input_data

max = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def game_ok(max_game):
    for color, i in max_game.items():
        if i > max[color]:
            return False
    return True

def game_max(plays):
    max_game = dict()
    for play in plays:
        takes = [x.strip() for x in play.split(',')]
        for take in takes:
            i, color = [x.strip() for x in take.split(' ')]
            if color not in max_game:
                max_game[color] = int(i)
            else:
                if max_game[color] < int(i):
                    max_game[color] = int(i)
    print(max_game)
    return max_game


def play_ok(play):
    takes = [x.strip() for x in play.split(',')]
    for take in takes:
        i, color = [x.strip() for x in take.split(' ')]
        if int(i) > max[color]:
            return False
    return True

sum = 0
sum2 = 0

for game in input_data.splitlines():
    gamename, allplays = [x.strip() for x in game.split(':')]
    _, gamenumber = [x.strip() for x in gamename.split(' ')]
    plays = [x.strip() for x in allplays.split(';')]
    max_game = game_max(plays)

    if game_ok(max_game):
        sum += int(gamenumber)

    power = 1
    for key, value in max_game.items():
        power = power * value
    print(power)
    sum2 += power

print(sum)
print(sum2)
puzzle.answer_a = sum
puzzle.answer_b = sum2
