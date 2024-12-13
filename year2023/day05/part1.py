import re

with open('input') as f:
    input = f.readlines()
    
# parsing seeds
seeds = [int(x) for x in re.findall(r'\d+', input[0])]

# parsing maps
maps_str = re.findall(r'[a-z-\s:]+\n([0-9\s]+)', ''.join(input[2:]))
maps = []
for map_str in maps_str:
    map = []
    for line in map_str.split('\n'):
        d = re.findall(r'\d+', line)
        if len(d) == 3:
            map.append([int(d[0]), int(d[1]), int(d[2])])
    maps.append(map)

# computing
dests = []
for seed in seeds:
    n = seed
    for map in maps:
        dest = n
        for line in map:
            dest_start = line[0]
            src_start = line[1]
            range = line[2]
            if src_start <= n <= src_start + range:
                dest = n + dest_start - src_start
                break
        n = dest
    dests.append(n)

print(min(dests))