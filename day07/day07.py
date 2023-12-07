from aocd.models import Puzzle
from collections import Counter

puzzle = Puzzle(year=2023, day=7)
input_data = puzzle.examples[0].input_data
input_data = puzzle.input_data

order_a = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
order_a.reverse()

order_b = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
order_b.reverse()

def card_type_a(cards):
    counted = Counter(cards)
    values = list(counted.values())
    values.sort(reverse=True)
    if values[0] == 5:
        return 7 # Five of a kind
    if values[0] == 4:
        return 6 # Four of a kind
    if values[0] == 3 and values[1] == 2:
        return 5 # Full house
    if values[0] == 3:
        return 4 # Three of a kind
    if values[0] == 2 and values[1] == 2:
        return 3 # Two pair
    if values[0] == 2:
        return 2 # One pair
    return 1 # High card

def card_value(cards, order, card_type):
    base = len(order)
    v = pow(base, 6) * card_type(cards)
    for i in range(0, len(cards)):
        b = cards[i]
        bv = order.index(b)
        nv = pow(base, len(cards) - i) * bv
        v +=  nv
    return v

result_a = []
players = input_data.splitlines()
for player in players:
    hand, bid = player.split()
    cv = card_value(hand, order_a, card_type_a)
    result_a.append((hand, bid, cv))

def takeCardValue(elem):
    return elem[2]

result_a.sort(key=takeCardValue)

sum_a = 0
for i in range(len(result_a)):
    r = result_a[i]
    sum_a += (i+1) * int(r[1])
print(sum_a)
puzzle.answer_a = sum_a


def card_type_b(cards):
    counted = Counter(cards)
    j = 0
    if "J" in counted:
        j = counted["J"]
        del counted["J"]
    values = list(counted.values())
    values.sort(reverse=True)
    if j == 5 or values[0] + j >= 5:
        return 7 # Five of a kind
    if values[0] + j >= 4:
        return 6 # Four of a kind
    if (values[0] >= 3 and values[1] >= 2 
        or (j == 1 
            and ((values[0] >= 2 and values[1] >= 2) or (values[0] >= 3 and values[1] >= 1))
        )
        or (j == 2
            and ((values[0] >= 1 and values[1] >= 2) or (values[0] >= 3 and values[1] >= 0))
        )
    ):
        return 5 # Full house
    if values[0] + j >= 3:
        return 4 # Three of a kind
    if (values[0] == 2 and values[1] == 2
        or (j == 1 
            and ((values[0] >= 1 and values[1] >= 2) or (values[0] >= 2 and values[1] >= 1))
        )
        ):
        return 3 # Two pair
    if values[0] + j >= 2:
        return 2 # One pair
    return 1 # High card

result_b = []
for player in players:
    hand, bid = player.split()
    cv = card_value(hand, order_b, card_type_b)
    result_b.append((hand, bid, cv))

result_b.sort(key=takeCardValue)

sum_b = 0
for i in range(len(result_b)):
    r = result_b[i]
    sum_b += (i+1) * int(r[1])
print(sum_b)
puzzle.answer_b = sum_b
