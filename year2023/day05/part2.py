import re

# seeds are sets
# sets have a start and an end
# maps are a list of mappings
# mappings have a set and a delta_to_apply
# assume all mappings within a map are disjoints

# intersection btw 2 sets
# set1: [0,10], set2: [5,15] => [5,10]
def inter(set1, set2):
    if set1[1] < set2[0] or set2[1] < set1[0]:
        return []
    start = max(set1[0], set2[0])
    end = min(set1[1], set2[1])
    return [start, end]

# 1-to-1 intersections btw a set and multiple others
# input: [0,10], sets: [[5,15], [-2,0], [20,25]] => [[5,10], [0,0], []]
def inter_with_multiple(input, sets):
    return [inter(input,s) for s in sets]

# returns the sets required to "fill the gaps" between sets within the "big" set
# sets: [[2,3], [4,5], [7,8]], big_set: [0,12] => [[0,1], [6,6], [9,12]]
def fill_btw_sets(sets, big_set):
    if sets == []: return [big_set]
    sets = [s for s in sets if s != []]
    sets = sorted(sets, key=lambda x: x[0]) # sorts sets
    fill = []
    if big_set[0] < sets[0][0]: # fill between big set start and 1st set start
        fill.append([big_set[0], sets[0][0]-1])
    if sets[len(sets)-1][1] < big_set[1]: # fill between last set end and big set end
        fill.append([sets[len(sets)-1][1]+1, big_set[1]])
    for i in range(0, len(sets)-1): # fill between sets
        fill_start = sets[i][1]+1
        fill_end = sets[i+1][0]-1
        if fill_start <= fill_end:
            fill.append([fill_start, fill_end])
    return fill
        
# apply a map to a set (unspecified mapping => identity mapping)
# note: 1 input set, 1+ output sets
def map_set (input_set, mappings):
    mappings_sets = [[m[0], m[1]] for m in mappings] # sets of mappings
    
    restricted_mappings_sets = inter_with_multiple(input_set, mappings_sets) # sets of mappings, restricted within the input set
    restricted_mappings = [[restricted_mappings_sets[i][0], restricted_mappings_sets[i][1], mappings[i][2]] for i in range(0,len(mappings)) if restricted_mappings_sets[i] != []] # new mappings
    
    fill_sets = fill_btw_sets([x for x in restricted_mappings_sets if x != []], input_set) # sets contained within the input set, but not included in any mapping set
    fill_mappings = [[s[0], s[1], 0] for s in fill_sets] # mappings with 0 delta
    all_mappings = restricted_mappings + fill_mappings

    output_sets = [[m[0]+m[2], m[1]+m[2]] for m in all_mappings] # mapped input_set ! 
    return output_sets

# apply map_set to a list of input_sets
def map_sets (input_sets, mappings):
    output_sets = []
    for input_set in input_sets:
        output_sets += map_set(input_set, mappings)
    return output_sets
        

with open('input') as f:
    input = f.readlines()
    
# parsing seeds: [start, end]
seeds_n = [int(x) for x in re.findall(r'\d+', input[0])]
seeds = []
i = 0
while i < len(seeds_n)-1:
    seeds.append([seeds_n[i], seeds_n[i]+seeds_n[i+1]])
    i += 2

# parsing maps: [src_start, src_end, delta_to_apply]
maps_str = re.findall(r'[a-z-\s:]+\n([0-9\s]+)', ''.join(input[2:]))
maps = []
for map_str in maps_str:
    map = []
    for line in map_str.split('\n'):
        d = re.findall(r'\d+', line)
        if len(d) == 3:
            map.append([int(d[1]), int(d[1])+int(d[2]), int(d[0])-int(d[1])])
    maps.append(map)

sets = seeds
i = 0
for map in maps:
    sets = map_sets(sets, map)
    i+=1

print(min(min(sets)))