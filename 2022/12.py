

import sys
import string

def parse_input(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    lines = content.strip().split("\n")
    lines = [ list(x) for x in lines]
    return lines

INFINITE = 9999999999999999
filename = sys.argv[1]
lines = parse_input(filename)
chars =  list(string.ascii_lowercase)

def printmap(pos,m):
    global tentative_distances
    print("   ")
    for y,line in enumerate(m):
        for x,col in enumerate(line):
            if pos[0] == y and pos[1] == x:
                print("@", end="")
            elif (y,x) not in unvisited:
                print(".", end="")
                #print(str(tentative_distances[(y,x)]), end="")
            else:
                print(col, end="")
        print("")
    print("   ")
    

heightmap = lines
height = len(lines)
width = len(lines[0])

for y,line in enumerate(heightmap):
    for x,col in enumerate(line):
        if heightmap[y][x] == 'E':
            #dest = (y,x) #part1
            start = (y,x) #part2
            heightmap[y][x] = 'z'

for y,line in enumerate(heightmap):
    for x,col in enumerate(line):
        if heightmap[y][x] == 'S':
            #start = (y,x) #part1
            dest = (y,x) #part2
            heightmap[y][x] = 'a'

unvisited = set()
for y,line in enumerate(heightmap):
    for x,col in enumerate(line):
        unvisited.add((y,x))

tentative_distances = {}
for y,line in enumerate(heightmap):
    for x,col in enumerate(line):
        tentative_distances[(y,x)] = INFINITE


current_node = start
posy = current_node[0]
posx = current_node[1]
tentative_distances[(posy,posx)] = 0
prev = {}
weight = 1

def update_neighbour(ny,nx,current_dist,current_node):
    newdist = INFINITE

    if ny >= 0 and ny <= height and nx >= 0 and nx <= width and (ny,nx) in unvisited:

        elevation =  chars.index(heightmap[current_node[0]][current_node[1]]) - chars.index(heightmap[ny][nx])
        if elevation > 1:
            return INFINITE

        value = heightmap[ny][nx]
        olddist = tentative_distances[(ny,nx)]
        newdist = current_dist + weight
        if newdist < olddist:
            tentative_distances[(ny,nx)] = newdist
            prev[(ny,nx)]= current_node
    return newdist
    
while len(unvisited) > 0:
    posy = current_node[0]
    posx = current_node[1]

    #if posy == dest[0] and posx == dest[1]: #part1
    if heightmap[posy][posx] == 'a': #part2
        print("loppu")
        break;

    current_dist = tentative_distances[(posy,posx)]
    unvisited.remove(current_node)

    #south
    ny = posy+1
    nx = posx
    dist = update_neighbour(ny,nx,current_dist,current_node)

    #north
    ny = posy-1
    nx = posx
    dist = update_neighbour(ny,nx,current_dist,current_node)

    #east
    ny = posy
    nx = posx+1
    dist = update_neighbour(ny,nx,current_dist,current_node)

    #west
    ny = posy
    nx = posx-1
    dist = update_neighbour(ny,nx,current_dist,current_node)


    #Find the next smallest uvisited node
    smallest = [current_dist,INFINITE]
    for k in tentative_distances:
        v = tentative_distances[k]
        if v<smallest[1] and k in unvisited:
            smallest[1]=v
            smallest[0]=k
    current_node = smallest[0]
    #printmap(current_node,heightmap)


#Shortest path:
s = []
c = prev[current_node]
s.append(c)
while c in prev:
    c = prev[c]
    s = [c] + s
s.append(current_node)
print("---")
print(len(s)-1)


