import re

def isGear (str):
    return str == '*'

with open('input') as f:
    input = f.readlines()
    
chars = [c for c in input]

width = len(input[0])
height = len(input)

gears_parts = [[[] for _ in range(0,width)] for _ in range(0,height)]

for l in range(0,len(chars)):
    line = chars[l]
    c = 0
    while c < len(line):
        subline = line[c:]
        match = re.findall(r'^\d+', subline)
        
        # we retrieved a number
        if match != []:
            n_str = match[0]
            n_len = len(n_str)
            n_int = int(n_str)
            
            adj_gears = []
            
            # check if gears are near the number. If so, memorize the gears's positions
            if (c > 0) and isGear(line[c-1]): adj_gears.append([l, c-1]) # before n
            if (c + n_len < width-1) and isGear(line[c+n_len]): adj_gears.append([l, c+n_len]) # after n
            if (l > 0): 
                for i in range(c, c+n_len):
                    if isGear(chars[l-1][i]): adj_gears.append([l-1, i]) # above n
                if (c > 0) and isGear(chars[l-1][c-1]): adj_gears.append([l-1, c-1]) # before (above n)
                if (c + n_len < width-1) and isGear(chars[l-1][c+n_len]): adj_gears.append([l-1, c+n_len]) # after (above n)
            if (l < height-1): 
                for i in range(c, c+n_len):
                    if isGear(chars[l+1][i]): adj_gears.append([l+1, i]) # under n
                if (c > 0) and isGear(chars[l+1][c-1]): adj_gears.append([l+1, c-1]) # before (under n)
                if (c + n_len < width-1) and isGear(chars[l+1][c+n_len]): adj_gears.append([l+1, c+n_len]) # after (under n)
                
            # for each adjacent gear, we add the number to this gear's parts
            for adj in adj_gears:
                gears_parts[adj[0]][adj[1]].append(n_int)
                
            c += n_len # if n=256, do not process 56 and 6
        
        c += 1

sum = 0
for l in gears_parts:
    for c in l:
        if len(c) == 2: # we only sum gears with exactly 2 parts !
            sum += c[0] * c[1]
            
print(sum)