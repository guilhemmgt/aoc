class Pos:
    x : int
    y : int
    def __init__ (self, y, x):
        self.x = x
        self.y = y
    def __str__ (self):
        return str(self.y) + ";" + str(self.x)
    def __eq__(self, value):
        return value.x == self.x and value.y == self.y

def up(p): return Pos(p.y-1, p.x)
def down(p): return Pos(p.y+1, p.x)
def right(p): return Pos(p.y, p.x+1)
def left(p): return Pos(p.y, p.x-1)
def symbol(p):
    if is_in_grid(p):
        return grid[p.y][p.x]
    else:
        return None
def is_in_grid(p):
    return 0 <= p.x <= x_max and 0 <= p.y <= y_max

def getTrailEnds(start_pos):
    if symbol(start_pos) == 9:
        return [start_pos] 
    else:
        neighborsEnds = []
        dir = [up, down, right, left]
        for d in dir:
            if symbol(d(start_pos)) == symbol(start_pos) + 1:
                neighborsEnds += getTrailEnds(d(start_pos))
        return neighborsEnds

def main():
    with open('input') as f:
        input = f.readlines()
        
    # parse input into array of array of chars
    global grid; grid = [ [int(c) for c in line if c != '\n'] for line in input]
    global y_max; y_max = len(grid)-1
    global x_max; x_max = len(grid[0])-1

    # retrieves trailheads
    trailheads = []
    for y in range(0,y_max+1):
        for x in range(0,x_max+1):
            p = Pos(y,x)
            if symbol(p) == 0:
                trailheads.append(p)

    # computes
    res = 0
    for th in trailheads:
        ends = getTrailEnds(th)
        uniqueEnds = []
        for e in ends:
            if not e in uniqueEnds:
                uniqueEnds.append(e)
        res += len(uniqueEnds)
    
    print(res)
        
if __name__ == '__main__':
    main()