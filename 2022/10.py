

import sys
import string

def parse_input(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    lines = content.strip().split("\n")
    lines = [x.split(' ') for x in lines]
    return lines

filename = sys.argv[1]
lines = parse_input(filename)

cycle = 0
xreg = 1
result_part_1 = 0

row = "."*40
screen = [ list(row) for i in range(0,6) ]

def print_screen(screen):
    print("")
    print("\n".join( [ "".join(s) for s in screen]))
    print("")

def clock(cycle):
    global result_part_1
    y = int(cycle / 40)
    x = int(cycle % 40)
    if x >= xreg-1 and x <= xreg+1:
        screen[y][x] ="#"
    print_screen(screen)
    cycle += 1
    if cycle == 20 or (cycle % 40) == 20:
        result_part_1 += cycle*x
    return cycle

for line in lines:
    cycle = clock(cycle)
    if line[0] == "addx":
        cycle = clock(cycle)
    if line[0] == "addx":
        xreg += int(line[1])

print(result_part_1)

