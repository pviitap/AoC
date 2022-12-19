

import sys
import string

def parse_input(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    lines = content.strip().split("\n\n")
    lines = [ tuple(x.split('\n')) for x in lines]
    return lines

filename = sys.argv[1]
lines = parse_input(filename)

for line in lines:
    left = line[0]
    rigth = line[0]
    



print(lines)
