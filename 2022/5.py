
import sys
import string
import re

def parse_input(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    parts = content.split("\n\n")
    return parts

def transpose_text(text):
    s = [ list(x) for x in text]

    ## transpose with numpy:
    #s = np.array(list(s))
    #s = s.transpose()
    #s = s.tolist()

    s = list(zip(*s))    #transpose
    s = "\n".join([ "".join(x)[::-1] for x in s ])
    return s

def construct_stack(text):
    stacks = text.split("\n")
    s = transpose_text(stacks)
    s = s.replace("[","").replace("]","").replace("\n","")
    s = s.split()
    stacks = {}
    for x in s:
        stacks[re.findall(r'\d',x)[0]] = list(re.findall(r'\D.*',x)[0])
    return stacks

filename = sys.argv[1]
parts = parse_input(filename)


stacks = construct_stack(parts[0])
instructions = parts[1].strip().split("\n")
for instruction in instructions:
    #numbers = re.findall(r'\d+',instruction)
    numbers = re.findall(r'^move (\d+) from (\d+) to (\d+)$',instruction)[0]
    times = int(numbers[0])
    move_from = numbers[1]
    move_to = numbers[2]
    for i in range(0,times):
        x = stacks[move_from].pop()
        stacks[move_to].append(x)

result = [ stacks[x].pop() for x in stacks.keys() ]
print("".join(result))

stacks = construct_stack(parts[0])
instructions = parts[1].strip().split("\n")
for instruction in instructions:
    #numbers = re.findall(r'\d+',instruction)
    numbers = re.findall(r'^move (\d+) from (\d+) to (\d+)$',instruction)[0]
    times = int(numbers[0])
    move_from = numbers[1]
    move_to = numbers[2]
    start = len(stacks[move_from])-times
    temp = stacks[move_from][start:]
    for i in range(0,times):
        stacks[move_from].pop()
    for t in temp:
        stacks[move_to].append(t)

result = [ stacks[x].pop() for x in stacks.keys() ]
print("".join(result))
