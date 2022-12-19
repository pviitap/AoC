import sys
import string


def parse_input(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    lines = content.strip().split("\n")
    lines = [x for x in lines]
    return lines


filename = sys.argv[1]
lines = parse_input(filename)
instructions = [tuple(x.split(",")) for x in lines]
instruction_pairs = [
    ((int(a.split("-")[0]), int(a.split("-")[1])), (int(b.split("-")[0]), int(b.split("-")[1])))
    for a, b in instructions]

pairs_fully_containing_another = list \
    (filter(lambda x: (x[1][0] <= x[0][0] and x[1][1] >= x[0][1]) or (x[0][0] <= x[1][0] and x[0][1] >= x[1][1]),
            instruction_pairs))
print(len(pairs_fully_containing_another))

pairs_partially_containing_another = list \
    (filter(lambda x: (x[1][0] <= x[0][1] and x[1][1] >= x[0][0]), instruction_pairs))
print(len(pairs_partially_containing_another))

## Or with sets:
#instruction_pairs = [
#    (set(range(int(a.split("-")[0]), int(a.split("-")[1]) + 1)),
#     set(range(int(b.split("-")[0]), int(b.split("-")[1]) + 1)))
#    for a, b in instructions]
#pairs_fully_containing_another = list(
#    filter(lambda x: x[0].issuperset(x[1]) or x[1].issuperset(x[0]), instruction_pairs))
#print(len(pairs_fully_containing_another))
#pairs_partially_containing_another = list(
#    filter(lambda x: len(x[0].intersection(x[1])) > 0 or len(x[1].intersection(x[0])) > 0, instruction_pairs))
#print(len(pairs_partially_containing_another))
