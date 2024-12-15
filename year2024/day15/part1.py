# element wise addition
def ew_add(l1, l2):
    return [sum(x) for x in zip(l1, l2)]

# recursively check if move(current, dir) is coherent
def can_move(current, dir):
    dest = ew_add(current, dir)
    dest_symbol = grid[dest[0]][dest[1]]
    match dest_symbol:
        case '#': return False
        case '.': return True
        case 'O': return can_move(dest, dir)

# recursively move objects
# precondition: can_move(current,dir)
def move(current, dir):
    dest = ew_add(current, dir)
    dest_symbol = grid[dest[0]][dest[1]]
    match dest_symbol:
        case '.':
            grid[dest[0]][dest[1]] = grid[current[0]][current[1]]
            grid[current[0]][current[1]] = '.'
        case 'O':
            move(dest, dir)
            grid[dest[0]][dest[1]] = grid[current[0]][current[1]]
            grid[current[0]][current[1]] = '.'

def main():
    with open('input') as f:
        input = f.read()
        
    # parse instructions list
    instructions = ''.join(input.split('\n\n')[1]).replace('\n','')
    
    # parse grid
    global grid; grid = [[c for c in l] for l in input.split('\n\n')[0].split('\n')]
    global y_size; y_size = len(grid)
    global x_size; x_size = len(grid[0])
    
    # get robot starting pos
    robot = []
    for y in range(0, y_size):
        for x in range(0, x_size):
            if grid[y][x] == '@':
                robot = [y,x]
                break
        if robot != []:
            break
    
    # compute
    for instr in instructions:
        match instr:
            case '^': dir = [-1,0]
            case '>': dir = [0,1]
            case 'v': dir = [1,0]
            case '<': dir = [0,-1]
        if can_move(robot, dir):
            move(robot, dir)            # change grid
            robot = ew_add(robot, dir)  # keep track of the robot position
            
    # find boxes
    res = 0
    for y in range(0, y_size):
        for x in range(0, x_size):
            if grid[y][x] == 'O':
                res += y*100 + x
        
    print(res)
        
if __name__ == '__main__':
    main()