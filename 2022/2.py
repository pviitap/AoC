import sys


def parse_input(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    lines = content.strip().split("\n")
    lines = [x for x in lines]
    return lines


scoring = {'X': 1, 'Y': 2, 'Z': 3}

win = 6
draw = 3
lose = 0

rules = {
    'A X': draw,
    'A Y': win,
    'A Z': lose,
    'B X': lose,
    'B Y': draw,
    'B Z': win,
    'C X': win,
    'C Y': lose,
    'C Z': draw,
}

filename = sys.argv[1]
strategy_guide = parse_input(filename)
total = 0
for line in strategy_guide:
    score1 = scoring[line.split(' ')[1]]
    score2 = rules[line]
    total += score1 + score2
print(total)

fixed_rules = {
    'A X': 'A Z',
    'A Y': 'A X',
    'A Z': 'A Y',
    'B X': 'B X',
    'B Y': 'B Y',
    'B Z': 'B Z',
    'C X': 'C Y',
    'C Y': 'C Z',
    'C Z': 'C X',
}
total = 0
for line in strategy_guide:
    line = fixed_rules[line]
    score1 = scoring[line.split(' ')[1]]
    score2 = rules[line]
    total += score1 + score2
print(total)
