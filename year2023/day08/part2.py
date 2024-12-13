import re
import numpy as np

# stupid LCM >:(

def run_from(start):
    steps = 0
    current_node = start
    while not current_node.endswith('Z'):
        for inst in instructions:
            current_node = nodes[current_node][inst]
            steps += 1
            if current_node.endswith('Z'):
                break
    return steps

with open('input') as f:
    input = f.readlines()

# parse instructions as ints (L=0, R=1)
instructions = []
for i in input[0]:
    if i == 'L': instructions.append(0)
    elif i == 'R': instructions.append(1)

# parse nodes as a dictionnary of [L, R]
nodes = {}
for node in input[2:]:
    matches = re.findall(r'[A-Z]+', node)
    nodes[matches[0]] = [matches[1], matches[2]]
    
# compute
starting_nodes = [x for x in nodes if x.endswith('A')]
steps = [run_from(n) for n in starting_nodes]
print(np.lcm.reduce(steps))
