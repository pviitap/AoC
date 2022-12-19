

import sys

def parse_input(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    lines = content.strip().split("\n")
    return lines

def find_unique_chars(text,length):
    i=length-1
    while True:
        i+=1
        chars = []
        for x in range(0,length):
            chars.append(text[x])
        if len(set(chars)) == length:
            return i
        text= text[1:]

filename = sys.argv[1]
lines = parse_input(filename)
message = list(lines[0])

print(find_unique_chars(message,4))
print(find_unique_chars(message,14))
