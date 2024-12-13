import re

# all positions are [y,x]

# nul à chier bouh recommence depuis le début c'est pas du petit scripting

def up(pos): return[pos[0]-1,pos[1]]
def down(pos): return[pos[0]+1,pos[1]]
def right(pos): return[pos[0],pos[1]+1]
def left(pos): return[pos[0],pos[1]-1]

def pickNextPos(pos_from, pos_current, pick=0):
    y, x = pos_current
    tile_current = maze[y][x]
    # two ends of the current tile pipe
    lookUp = []
    match tile_current:
        case '|': lookUp = [ up(pos_current), down(pos_current) ]
        case '-': lookUp = [ left(pos_current), right(pos_current) ]
        case 'L': lookUp = [ up(pos_current), right(pos_current) ]
        case 'J': lookUp = [ up(pos_current), left(pos_current) ]
        case '7': lookUp = [ down(pos_current), left(pos_current) ]
        case 'F': lookUp = [ down(pos_current), right(pos_current) ]
    # eliminate out of bounds positions + 'from' position
    lookUp = [p for p in lookUp if 0<=p[0]<=y_max and 0<=p[1]<=x_max and p != pos_from]
    # return next pos (if it exists)
    return lookUp[pick]

with open('input') as f:
    input = f.readlines()

# parse input into array of array of chars
maze = [ [c for c in line if c != '\n'] for line in input]
y_max = len(maze)-1
x_max = len(maze[0])-1

# find start location
y_start = 0
x_start = 0
for x in range(0,x_max):
    done = False
    for y in range(0,y_max):
        if maze[y][x] == 'S':
            y_start = y
            x_start = x
            done = True
            break
    if done: break
    
pos_start = [y_start, x_start]
up_from_start, down_from_start, left_from_start, right_from_start = up(pos_start), down(pos_start), left(pos_start), right(pos_start)
if maze[up_from_start[0]][up_from_start[1]] == '|' or maze[up_from_start[0]][up_from_start[1]] == 'F' or maze[up_from_start[0]][up_from_start[1]] == '7':
    pos_current = up_from_start
elif maze[down_from_start[0]][down_from_start[1]] == '|' or maze[down_from_start[0]][down_from_start[1]] == 'J' or maze[down_from_start[0]][down_from_start[1]] == 'L':
    pos_current = down_from_start
elif maze[left_from_start[0]][left_from_start[1]] == '-' or maze[left_from_start[0]][left_from_start[1]] == 'F' or maze[left_from_start[0]][left_from_start[1]] == 'L':
    pos_current = left_from_start
else:
    pos_current = right_from_start
pos_from = pos_start
path = []
while maze[pos_current[0]][pos_current[1]] != 'S':
    path.append(pos_current)
    pos_next = pickNextPos(pos_from, pos_current)
    pos_from = pos_current
    pos_current = pos_next
    
print(int((len(path)+1)/2))