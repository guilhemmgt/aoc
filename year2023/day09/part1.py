import re
    
def findDelta(seq):
    delta = []
    for i in range(0, len(seq)-1):
        delta.append(seq[i+1]-seq[i])
    return delta

def isAllZeroesOrSingleton(seq):
    return all(x == 0 for x in seq)

with open('input') as f:
    input = f.readlines()

# parsing
input = [[int(x) for x in re.findall(r'-?\d+', line)] for line in input]
    
res = 0
for line in input:
    seqs = [line]
    while not isAllZeroesOrSingleton(seqs[len(seqs)-1]):
        seqs.append(findDelta(seqs[len(seqs)-1]))
        
    extrapolated = sum([seq[len(seq)-1] for seq in seqs])
    
    res += extrapolated
    
print('res:', res)