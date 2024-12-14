import re
import math

SIZE_X = 101
SIZE_Y = 103
TARGET_TIME = 100

class Robot:
    px, py, vx, vy = 0, 0, 0, 0
    def __init__ (self, init):
        self.px, self.py, self.vx, self.vy = init
    def move(self):
        self.px = (self.px + self.vx) % SIZE_X
        self.py = (self.py + self.vy) % SIZE_Y

def main():
    with open('input') as f:
        input = f.readlines()
    
    # parse + init
    robots = [Robot([int(x) for x in re.findall(r'-?\d+', line)]) for line in input] # robot = [px, py, vx, vy]
    
    # compute
    for s in range(0, TARGET_TIME):
        for r in robots: # could have directly computed the position instead of iterating ...
            r.move() 
            
    # result (ugly)
    quadrants = [0,0,0,0]
    for r in robots:
        if r.py < (SIZE_Y-1)/2: # north
            if r.px < (SIZE_X-1)/2: # west
                quadrants[0] += 1
            elif r.px > (SIZE_X-1)/2: # east
                quadrants[1] += 1
        elif r.py > (SIZE_Y-1)/2: # south
            if r.px < (SIZE_X-1)/2: # west
                quadrants[2] += 1
            elif r.px > (SIZE_X-1)/2: # east
                quadrants[3] += 1
    result = math.prod(quadrants)
        
    print(result)
        
if __name__ == '__main__':
    main()