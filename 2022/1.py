import sys


def parse_input(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    lines = content.strip().split("\n\n")
    lines = [[int(x) for x in line.split("\n")] for line in lines]
    return lines


filename = sys.argv[1]
lines = parse_input(filename)

sums = [sum(line) for line in lines]
print(max(sums))
sums.sort(reverse=True)
print(sums[0] + sums[1] + sums[2])
