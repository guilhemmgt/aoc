class Pos:
    x : int
    y : int
    def __init__ (self, y, x):
        self.x = x
        self.y = y
    def __str__ (self):
        return str(self.y) + ";" + str(self.x)

def up(p): return Pos(p.y-1, p.x)
def down(p): return Pos(p.y+1, p.x)
def right(p): return Pos(p.y, p.x+1)
def left(p): return Pos(p.y, p.x-1)

def symbol(p):
    if 0 <= p.x <= x_max and 0 <= p.y <= y_max:
        return grid[p.y][p.x]
    else:
        return None

def check_x(p, upleft, upright, downright, downleft):
    return symbol(p)=='A' and symbol(up(left(p)))==upleft and symbol(up(right(p)))==upright and symbol(down(right(p)))==downright and symbol(down(left(p)))==downleft

def check(p):
    return check_x(p, 'M','S','S','M') + check_x(p, 'M','M','S','S') + check_x(p, 'S','M','M','S') + check_x(p, 'S','S','M','M')

with open('input') as f:
    input = f.readlines()
    
# parse input into array of array of chars
grid = [ [c for c in line if c != '\n'] for line in input]
y_max = len(grid)-1
x_max = len(grid[0])-1

res = 0
for y in range(0,y_max+1):
    for x in range(0,x_max+1):
        p = Pos(y,x)
        
        if symbol(p) == 'A':
            res += check(p)
                
print(res)