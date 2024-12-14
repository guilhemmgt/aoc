import re
import statistics

# hated this challenge

# found christmas tree by finding minimal position standard deviation for both coordinates
# (got the idea before even looking on reddit :) )

SIZE_X = 101
SIZE_Y = 103
TARGET_TIME = SIZE_X*SIZE_Y # robots loop after SIZE_X*SIZE_Y seconds because of the modulos

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
    init_robots = [Robot([int(x) for x in re.findall(r'-?\d+', line)]) for line in input]
    
    # compute
    stdevs = []
    for s in range(0, TARGET_TIME):
        stdevs.append(statistics.stdev([r.px for r in robots]) + statistics.stdev([r.py for r in robots]))
        for r in robots:
            r.move()
            
    # result
    min_stdev = min(stdevs)
    min_stdev_s = stdevs.index(min_stdev)
    
    print(min_stdev_s)
        
        
if __name__ == '__main__':
    main()