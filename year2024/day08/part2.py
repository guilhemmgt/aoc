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
    def __add__(self, value):
        return Pos(self.y+value.y, self.x+value.x)
    def __sub__(self, value):
        return Pos(self.y-value.y, self.x-value.x)
    def __mul__(self, value):
        return Pos(self.y*value, self.x*value)

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
    
def add_antinode(p):
    if not p in unique_antinodes and is_in_grid(p):
        unique_antinodes.append(p)

def main():
    with open('input') as f:
        input = f.readlines()
        
    # parse input into array of array of chars
    global grid; grid = [ [c for c in line if c != '\n'] for line in input]
    global y_max; y_max = len(grid)-1
    global x_max; x_max = len(grid[0])-1
    
    # search all atennas
    antennas = {}
    for y in range(0, y_max+1):
        for x in range(0, x_max+1):
            p = Pos(y,x)
            s = symbol(p)
            if s != '.':
                if s in antennas:
                    antennas[s].append(p)
                else:
                    antennas[s] = [p]
                    
    # compute antinodes
    global unique_antinodes; unique_antinodes = []
    for frequency in antennas:
        for a1_pos in antennas[frequency]:
            for a2_pos in antennas[frequency]:
                if a1_pos == a2_pos: continue
                i=0
                while is_in_grid(a1_pos + (a1_pos-a2_pos)*i):
                    add_antinode(a1_pos + (a1_pos-a2_pos)*i)
                    i+=1
                i=0
                while is_in_grid(a2_pos + (a2_pos-a1_pos)*i):
                    add_antinode(a2_pos + (a2_pos-a1_pos)*i)
                    i+=1
                
    print(len(unique_antinodes))
        
if __name__ == '__main__':
    main()