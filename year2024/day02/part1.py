MIN_DELTA = 1
MAX_DELTA = 3

with open('input') as f:
    input = f.readlines()
    
sum = 0
    
for report in input:
    levels = [int(x) for x in report.split('\n')[0].split(' ')]
    legal = True
    
    increasing = levels[1]-levels[0] > 0
    
    for i in range(0, len(levels)-1):
        delta = levels[i+1]-levels[i]
        if (increasing and (MIN_DELTA <= delta <= MAX_DELTA)):
            continue
        elif (not increasing and (-MAX_DELTA <= delta <= -MIN_DELTA)):
            continue
        else:
            legal = False
            break
        
    if legal:
        sum += 1
        
print(sum)