

import sys
import string

def parse_input(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    lines = content.strip().split("\n")
    lines = [ list(x) for x in lines]
    return lines

filename = sys.argv[1]
lines = parse_input(filename)
print(lines)
