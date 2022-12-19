

import sys
import functools
import re
import string

def parse_input(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    lines = content.strip().split("\n\n")
    lines = [x for x in lines]
    return lines

filename = sys.argv[1]
lines = parse_input(filename)
monkeyLines = [ line.split("\n") for line in lines ]

class Monkey:
    inspect_count = 0
    items = []
    operation = None
    by = None
    test_divisible_by = None
    if_true_throw_to_monkey = None
    if_false_throw_to_monkey = None

    def __init__(self,items, operation, by, test_divisible_by, if_true_throw_to_monkey, if_false_throw_to_monkey):
        self.items = [ { "value": int(item), "stack": []}  for item in items]
        self.operation = operation

        if operation == '+':
            self.operation = 1
        elif operation == '*':
            self.operation = 2
        try:
            self.by = int(by[0])
        except ValueError:
            if operation == '+':
                self.operation = 3
            elif operation == '*':
                self.operation = 4

        self.test_divisible_by = int(test_divisible_by)
        self.if_true_throw_to_monkey = int(if_true_throw_to_monkey)
        self.if_false_throw_to_monkey = int(if_false_throw_to_monkey)

monkeys = [ Monkey( re.findall(r'\d+',line[1]), 
                    re.findall(r'[+,*]',line[2])[0],
                    re.findall(r'Operation: new = old [+,*] (.+)',line[2]),
                    re.findall(r'\d+',line[3])[0],
                    re.findall(r'\d+',line[4])[0],
                    re.findall(r'\d+',line[5])[0]
                    ) for line in monkeyLines ]

divisions = [ monkey.test_divisible_by for monkey in monkeys ]
max_val = functools.reduce(lambda x,y: x*y,divisions)
print(max_val)

for r in range(0,10000):
    for monkey in monkeys:
        for item in monkey.items:
            worry_level = item["value"]

            worry_level = worry_level % max_val

            monkey.inspect_count += 1

            if monkey.operation == 1: 
                worry_level = worry_level + monkey.by
            elif monkey.operation == 2:
                worry_level = worry_level * monkey.by
            elif monkey.operation == 3:
                worry_level = worry_level + worry_level
            elif monkey.operation == 4:
                worry_level = worry_level * worry_level
            else:
                throw("invalid operation")

            item["value"] = worry_level

            if worry_level % monkey.test_divisible_by == 0:
                monkeys[monkey.if_true_throw_to_monkey].items.append(item)
            else:
                monkeys[monkey.if_false_throw_to_monkey].items.append(item)
        monkey.items = []


inspect_counts = [ monkey.inspect_count for monkey in monkeys ]
print(inspect_counts)
inspect_counts.sort(reverse=True)
print(inspect_counts[0]*inspect_counts[1])
