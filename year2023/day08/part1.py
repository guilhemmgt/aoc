import re

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
steps = 0
current_node = 'AAA'
while current_node != 'ZZZ':
    for inst in instructions:
        current_node = nodes[current_node][inst]
        steps += 1
        if current_node == 'ZZZ':
            break
        
print(steps)