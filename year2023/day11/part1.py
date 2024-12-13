import re

def cloneRow(y, grid):
    grid.insert(y, grid[y])
    return grid
def cloneColumn(x, grid):
    for row in grid:
        row.insert(x, row[x])
    return grid

def isRowEmpty(y, grid):
    return all([e=='.' for e in grid[y]])
def isColumnEmpty(x, grid):
    return all([row[x]=='.' for row in grid])

def main():
    # open file
    with open('input') as f:
        input = f.readlines()
    # parse
    grid = [ [c for c in line if c != '\n'] for line in input]
    y_max = len(grid)-1
    x_max = len(grid[0])-1
    
    # expand the universe !
    empty_rows = [y for y in range(0,y_max+1) if isRowEmpty(y, grid)]
    empty_cols = [x for x in range(0,x_max+1) if isColumnEmpty(x, grid)]
    
    # TODO
    
if __name__ == '__main__':
    main()