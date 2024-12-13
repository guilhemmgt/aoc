class Dir:
    UP=0; DOWN=1; RIGHT=2; LEFT=3

class Pos:
    x : int
    y : int
    def __init__ (self, y, x):
        self.x = x
        self.y = y
    def __str__ (self):
        return str(self.y) + ";" + str(self.x)

def rotate_90(dir):
    match (dir):
        case Dir.UP: return Dir.RIGHT
        case Dir.DOWN: return Dir.LEFT
        case Dir.RIGHT: return Dir.DOWN
        case Dir.LEFT: return Dir.UP
    return None
def go(dir):
    match (dir):
        case Dir.UP: return up
        case Dir.DOWN: return down
        case Dir.RIGHT: return right
        case Dir.LEFT: return left
    return None
def up(p): return Pos(p.y-1, p.x)
def down(p): return Pos(p.y+1, p.x)
def right(p): return Pos(p.y, p.x+1)
def left(p): return Pos(p.y, p.x-1)
def symbol(p):
    if 0 <= p.x <= x_max and 0 <= p.y <= y_max:
        return grid[p.y][p.x]
    else:
        return None
    
def doesGuardLoop(start_pos, start_dir, extra_obstacle_pos):
    # add obstacle
    global grid; grid = [ [c for c in line if c != '\n'] for line in input]
    if extra_obstacle_pos != None: grid[extra_obstacle_pos.y][extra_obstacle_pos.x]='#'
    # init
    pos = start_pos
    dir = start_dir
    # compute
    history = [] # entire history (record pos+dir)
    looping = False
    while (symbol(pos) != None):
        # record pos and dir + detect looping
        current_state = [pos.y, pos.x, dir]
        if current_state in history:
            looping = True; break
        else:
            history.append(current_state)
        # move or rotate
        pos_ahead = go(dir)(pos)
        symbol_ahead = symbol(pos_ahead)
        if symbol_ahead == '#':
            dir = rotate_90(dir)
        else:
            pos = pos_ahead
            
    if looping:
        res += 1
            
def main():
    with open('input') as f:
        global input; input = f.readlines()
        
    # parse input into array of array of chars
    global grid; grid = [ [c for c in line if c != '\n'] for line in input]
    global y_max; y_max = len(grid)-1
    global x_max; x_max = len(grid[0])-1

    # init
    for x in range(0,x_max+1):
        for y in range(0,y_max+1): 
            if symbol(Pos(y,x))=='^': pos = Pos(y,x); break
    dir = Dir.UP
    
    # run part 1 to get the guard's path
    _, _, first_stepped = doesGuardLoop(pos, dir, None)

    global res; res = 0
            
    print(res)
        
if __name__ == '__main__':
    main()