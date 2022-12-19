

import sys
import string

def parse_input(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    lines = content.strip().split("\n")
    lines = [ x.split(' ') for x in lines]
    return lines

filename = sys.argv[1]
lines = parse_input(filename)

class Node:
    def __init__(self, name,size=0):
        self.name = name
        self.children = []
        self.size = size
        self.calculated_size = 0
    
    def add_child(self, node):
        self.children.append(node)
    def find_child(self, name):
        for child in self.children:
            if child.name == name:
                return child
    def __repr__(self):
        return self.name + " (" + str(self.size) + ")" +  " (" + str(self.calculated_size) + ")"



def print_node(depth,node):
    d = depth + 2
    for child in node.children:
        print(" "*d +"- " + repr(child))
        print_node(d,child)

def add_to_node(node,path,new_node):
    path = path.copy()
    if len(path)==1:
        node.add_child(new_node)
    else:
        del(path[0])
        for p in path:
            node = node.find_child(p)
        node.add_child(new_node)

def calculate_size(size,node):
    size += node.size
    for child in node.children:
        csize = calculate_size(0,child)
        size += csize
    node.calculated_size = size
    return size

root = Node('/')
path = []
for line in lines:
    #print(line)
    if line[0] == '$' and line[1] == 'cd' and line[2] != '..':
        current_dir = line[2]
        path.append(current_dir)
    if line[0] == '$' and line[1] == 'cd' and line[2] == '..':
        path.pop()
    if line[0] != '$' and line[0] == 'dir':
        add_to_node(root,path,Node(line[1]))
    if line[0] != '$' and line[0] != 'dir':
        filename = line[1]
        filesize = int(line[0])
        p = path.copy()
        add_to_node(root,p,Node(filename,filesize))

total = calculate_size(0,root)
#print_node(0,root)

def calculate_dirs_at_most_100k(size,node):
    if node.size == 0 and node.calculated_size <= 100000:
        size += node.calculated_size
    for child in node.children:
        size += calculate_dirs_at_most_100k(0,child)
    return size

print("Part 1: " + str(calculate_dirs_at_most_100k(0,root)))

TOTAL_DISK_SPACE = 70000000
SPACE_NEEDED_FOR_THE_UPDATE = 30000000

unused_space = TOTAL_DISK_SPACE - total
space_required = SPACE_NEEDED_FOR_THE_UPDATE - unused_space

def find_dir_to_delete(size,node,space_required):
    if node.size == 0 and node.calculated_size >= space_required:
        if (node.calculated_size < size): 
            size = node.calculated_size
    for child in node.children:
        size = find_dir_to_delete(size,child,space_required)
    return size

print("Part 2: " + str(find_dir_to_delete(TOTAL_DISK_SPACE,root,space_required)))
