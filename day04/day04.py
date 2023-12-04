from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=4)
input_data = puzzle.examples[0].input_data
input_data = puzzle.input_data

cardwins = dict()

sum1 = 0
sum2 = 0

for card in input_data.splitlines():
    values = [x.strip() for x in card.split(':')]
    cardnumber = [x.strip() for x in values[0].split(' ')][-1]
    my, matches_count = [x.strip() for x in values[1].split('|')]
    winners = [x.strip() for x in my.split(' ')]
    winners_set = set(winners)
    if '' in winners_set:
        winners_set.remove('')
    mys = [x.strip() for x in matches_count.split(' ')]
    mys_set = set(mys)
    if '' in mys_set:
        mys_set.remove('')

    matches = mys_set.intersection(winners_set)
    matches_count = len(winners_set.intersection(matches))
    cardwins[cardnumber] = matches_count

    if matches_count > 0:
        score = pow(2, matches_count-1)
        sum1 += score
    

print(sum1)
puzzle.answer_a = sum1


cardscount = [1 for i in range(len(cardwins))] 
for key, value in cardwins.items():
    cardnumber = int(key) -1
    r = range(cardnumber +1, cardnumber +1+ value)
    for i in r:
        cardscount[i] += cardscount[cardnumber]

sum2 = sum(cardscount)
print(sum2)
puzzle.answer_b = sum2
