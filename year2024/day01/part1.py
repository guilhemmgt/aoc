import re

with open('input') as f:
    input = f.readlines()

l1, l2 = [], []
for line in input:
    r = re.findall(r"\d+", line)
    l1.append((int)(r[0]))
    l2.append((int)(r[1]))
    
l1.sort()
l2.sort()

sum = sum([abs(l1[i] - l2[i]) for i in range(0,len(l1))])

print(sum)