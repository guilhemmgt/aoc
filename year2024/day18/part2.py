import heapq
import re

MAX_COOR = 70
MAX_TIME = 1024

# neighbors/directions always in order: north, east, south, west
# grid positions serves as nodes IDs in the graph

class Graph:
    neighbors = {} # [north, east, south, west]. None = no neighbor in this direction
    def __init__(self):
        self.neighbors = {}
    def get_cost(self, fromPos, toPos):
        return 1 if toPos in self.neighbors[fromPos] else None # if neighbors, distance=1; else, distance=None
        
def get_path(end, start, origin):
    path = [end]
    current = end
    while current != start:
        current = origin[current]
        path.append(current)
    return path
        
def ew_add(l1, l2):
    return tuple([sum(x) for x in zip(l1, l2)])

def main():
    with open('input') as f:
        input = f.read()
    
    # get obstacles positions
    obstacles = []
    digits = re.findall(r'\d+', input)
    i = 0
    while i < len(digits):
        obstacles.append((int(digits[i]), int(digits[i+1])))
        i += 2
        
    # add MAX_TIME obstacles
    current_obstacles = []
    for _ in range(0, MAX_TIME):
        current_obstacles.append(obstacles.pop(0))
        
    # get end and start positions
    start_pos = (0,0)
    end_pos = (MAX_COOR, MAX_COOR)

    success = True
    path = None
    while success:
        # add an obstacle
        new_obstacle = obstacles.pop(0)
        current_obstacles.append(new_obstacle)
        if path != None and (new_obstacle not in path):
            continue
        # construct a graph (yes, i should only update the graph locally but... good enough)
        graph = Graph()
        for y in range(0, MAX_COOR+1):
            for x in range(0, MAX_COOR+1):
                if (y,x) in current_obstacles: # walls are inaccessible
                    continue
                # we wil add pos [y,x] to the graph
                # we need to map its neighbors
                neighbors = []
                pos = (y,x)
                for dir in [(-1,0),(0,1),(1,0),(0,-1)]:
                    neighbor_pos = ew_add(pos, dir)
                    if not (0<=neighbor_pos[0]<=MAX_COOR and 0<=neighbor_pos[1]<=MAX_COOR): neighbors.append(None)
                    elif neighbor_pos in current_obstacles: neighbors.append(None)
                    else: neighbors.append(neighbor_pos)
                # done :)
                graph.neighbors[pos] = neighbors
        # search
        frontier = [] # priority queue of (priority, (y,x))
        origin = {}
        cost = {}
        heapq.heappush(frontier, (0, start_pos))
        origin[start_pos] = None
        cost[start_pos] = 0
        success = False
        while len(frontier) != 0:
            (_, current) = heapq.heappop(frontier)
            if current == end_pos:
                success = True
                break
            for neighbor in graph.neighbors[current]:
                if neighbor == None: continue
                current_cost_to_neighbor = cost[current] + graph.get_cost(current, neighbor)
                if (neighbor not in cost) or (current_cost_to_neighbor < cost[neighbor]):
                    heapq.heappush(frontier, (current_cost_to_neighbor, neighbor))
                    cost[neighbor] = current_cost_to_neighbor
                    origin[neighbor] = current
        # get path
        if success:
            path = get_path(end_pos, start_pos, origin)

    print(str(current_obstacles[-1][0]) + ',' + str(current_obstacles[-1][1]))
    
    
    
if __name__ == '__main__':
    main()