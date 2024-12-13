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

def main():
    with open('input') as f:
        input = f.readlines()
        
    # parse input into array of array of chars
    global grid; grid = [ [c for c in line if c != '\n'] for line in input]
    global y_max; y_max = len(grid)-1
    global x_max; x_max = len(grid[0])-1

    # init
    for x in range(0,x_max+1):
        for y in range(0,y_max+1): 
            if symbol(Pos(y,x))=='^': pos = Pos(y,x); break
    dir = Dir.UP
    
    # compute
    stepped = []
    while (symbol(pos) != None):
        if not [pos.y, pos.x] in stepped:
            stepped.append([pos.y, pos.x])
        pos_ahead = go(dir)(pos)
        symbol_ahead = symbol(pos_ahead)
        if symbol_ahead == '#':
            dir = rotate_90(dir)
        else:
            pos = pos_ahead
            
    print(len(stepped))
        
if __name__ == '__main__':
    main()