import re
import sys

# a plot of land: really just a wrapper for [char (=plant), int (=region)]
class Plot:
    plant : chr
    region : int
    def __init__ (self, plant):
        self.plant = plant
        self.region = None
    def __str__ (self):
        return "plant " + str(self.plant) + "; region " + str(self.region)

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
def get_plant(p):
    return grid[p.y][p.x].plant if is_in_grid(p) else None
def get_region(p):
    return grid[p.y][p.x].region if is_in_grid(p) else None
def set_region(p, r):
    if is_in_grid(p): grid[p.y][p.x].region = r
def is_in_grid(p):
    return 0 <= p.x <= x_max and 0 <= p.y <= y_max

def form_new_region_from_pos(p, id):
    region = [p]
    set_region(p, id)
    for dir in [up, down, right, left]:
        neighbor_pos = dir(p)
        if get_plant(neighbor_pos) == get_plant(p) and get_region(neighbor_pos) == None:
            region += form_new_region_from_pos(neighbor_pos, id)
    return region

def main():
    with open('input') as f:
        input = f.readlines()
        
    # parse input into array of array of Plots
    global grid; grid = [ [Plot(c) for c in line if c != '\n'] for line in input]
    global y_max; y_max = len(grid)-1
    global x_max; x_max = len(grid[0])-1

    # computes regions
    regions = []
    for y in range(0, y_max+1):
        for x in range(0, x_max+1):
            pos = Pos(y, x)
            if get_region(pos) == None:
                regions.append(form_new_region_from_pos(pos, len(regions)))
    
    # calculates prices
    price = 0
    for region in regions:
        area = len(region)
        perimeter = 0
        for pos in region:
            perimeter += sum([get_region(pos) != get_region(dir(pos)) for dir in [up, down, right, left]])
        price += area * perimeter
    
    print(price)
                
            
            
        
if __name__ == '__main__':
    main()