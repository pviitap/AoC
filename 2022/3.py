
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
chars =  list(string.ascii_lowercase) + list(string.ascii_uppercase)

rucksacks = [ ( x[:int(len(x)/2)],x[int(len(x)/2):len(x)] ) for x in lines]
common_items = [ list(filter( lambda y: y in x[0], x[1]))[0] for x in rucksacks ]
priorities = [ chars.index(x)+1 for x in common_items]
print(sum(priorities))

group_indexes = (list(range(0,len(lines),3)))
dwarf_groups = [ (lines[x:x+3]) for x in group_indexes]
common_items_groups = [ list( set(x[0]).intersection(set(x[1])).intersection(set(x[2])) ) for x in dwarf_groups]
common_items = [ x[0] for x in common_items_groups]
priorities = [ chars.index(x)+1 for x in common_items]
print(sum(priorities))


