import re

with open('input') as f:
    input = f.readlines()

l1, l2 = [], []
for line in input:
    r = re.findall(r"\d+", line)
    l1.append((int)(r[0]))
    l2.append((int)(r[1]))
    
score = sum([i1 * l2.count(i1) for i1 in l1])
    
print(score)