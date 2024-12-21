import heapq

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

def dir_changed(from_pos, current_pos, to_pos):
    if from_pos == None: from_pos = current_pos + (0, -1) # the player starts looking east
    current_dir = (current_pos[0] - from_pos[0], current_pos[1] - from_pos[1])
    to_dir = (to_pos[0] - current_pos[0], to_pos[1] - current_pos[1])
    return to_dir != current_dir

def main():
    with open('input') as f:
        input = f.read()
        
    # parse input as an array of arrays of char
    grid = [[c for c in l] for l in input.split('\n')]
    y_size = len(grid)
    x_size = len(grid[0])

    # get end and start positions
    start_pos = None
    end_pos = None
    for y in range(0, y_size):
        for x in range(0, x_size):
            if grid[y][x] == 'S': start_pos = (y,x)
            if grid[y][x] == 'E': end_pos = (y,x)

    # construct a graph
    graph = Graph()
    for y in range(0, y_size):
        for x in range(0, x_size):
            if grid[y][x] == '#': # walls are inaccessible
                continue
            # we wil add pos [y,x] to the graph
            # we need to map its neighbors
            neighbors = []
            pos = (y,x)
            for dir in [(-1,0),(0,1),(1,0),(0,-1)]:
                neighbor_pos = ew_add(pos, dir)
                if not (0<=neighbor_pos[0]<=y_size-1 and 0<=neighbor_pos[1]<=x_size-1): neighbors.append(None)
                neighbor_pos_symbol = grid[neighbor_pos[0]][neighbor_pos[1]]
                if neighbor_pos_symbol == '#': neighbors.append(None)
                if neighbor_pos_symbol in ['.', 'S', 'E'] : neighbors.append(neighbor_pos)
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
            rotation_cost = dir_changed(origin[current], current, neighbor) * 1000
            current_cost_to_neighbor = cost[current] + graph.get_cost(current, neighbor) + rotation_cost
            if (neighbor not in cost) or (current_cost_to_neighbor < cost[neighbor]):
                heapq.heappush(frontier, (current_cost_to_neighbor, neighbor))
                cost[neighbor] = current_cost_to_neighbor
                origin[neighbor] = current

    print(cost[end_pos])
    
if __name__ == '__main__':
    main()