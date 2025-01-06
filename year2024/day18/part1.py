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
        
def ew_add(l1, l2):
    return tuple([sum(x) for x in zip(l1, l2)])

def main():
    with open('input') as f:
        input = f.readlines()
    
    # get obstacles positions
    obstacles = []
    for i in range(0, MAX_TIME):
        digits = re.findall(r'\d+', input[i])
        obstacles.append((int(digits[1]), int(digits[0])))

    # get end and start positions
    start_pos = (0,0)
    end_pos = (MAX_COOR, MAX_COOR)

    # construct a graph
    graph = Graph()
    for y in range(0, MAX_COOR+1):
        for x in range(0, MAX_COOR+1):
            if (y,x) in obstacles: # walls are inaccessible
                continue
            # we wil add pos [y,x] to the graph
            # we need to map its neighbors
            neighbors = []
            pos = (y,x)
            for dir in [(-1,0),(0,1),(1,0),(0,-1)]:
                neighbor_pos = ew_add(pos, dir)
                if not (0<=neighbor_pos[0]<=MAX_COOR and 0<=neighbor_pos[1]<=MAX_COOR): neighbors.append(None)
                elif neighbor_pos in obstacles: neighbors.append(None)
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

    while len(frontier) != 0:
        (_, current) = heapq.heappop(frontier)
        if current == end_pos:
            break
        for neighbor in graph.neighbors[current]:
            if neighbor == None: continue
            current_cost_to_neighbor = cost[current] + graph.get_cost(current, neighbor)
            if (neighbor not in cost) or (current_cost_to_neighbor < cost[neighbor]):
                heapq.heappush(frontier, (current_cost_to_neighbor, neighbor))
                cost[neighbor] = current_cost_to_neighbor
                origin[neighbor] = current

    print(cost[end_pos])
    
if __name__ == '__main__':
    main()