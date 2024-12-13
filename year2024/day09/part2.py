def getFirstNFree(n, maxIdx):
    global startLookingForFreeIdx
    for i in range(startLookingForFreeIdx, maxIdx):
        id = memory[i]
        if id == None:
            if memory[startLookingForFreeIdx] != None: startLookingForFreeIdx = i
            # checks if this free space is at least n units long
            nFree = True
            for j in range(i, i+n):
                if memory[j] != None: nFree = False; break
            if nFree: # yipi
                return i
    return None

def getBlockLengthBackward(i):
    id = memory[i]
    n = 0
    j = i
    while j >= 0:
        if memory[j] != id: break
        n += 1
        j -= 1
    return n

def free(i, n):
    allocate(i, None, n)
def allocate(i, id, n):
    for j in range(i, i+n):
        memory[j] = id

def main():
    with open('input') as f:
        input = f.readlines()
        
    # parse
    global memory; memory = []
    freespace = False
    id = 0
    for l in input[0]:
        if l == '\n': continue
        for _ in range(0,int(l)):
            memory.append(id if not freespace else None)
        if freespace:
            id += 1
        freespace = not freespace
    
    # compute
    global startLookingForFreeIdx; startLookingForFreeIdx = 0
    i = len(memory)-1
    while i >= 0:
        id = memory[i]
        if id == None:
            i -= 1
        else:
            n = getBlockLengthBackward(i)
            freeIdx = getFirstNFree(n, i)
            if freeIdx != None:
                allocate(freeIdx, id, n)
                free(i-n+1, n)
            i -= n
    
    # checksum
    res = 0
    for i in range(0, len(memory)):
        id = memory[i]
        if id != None:
            res += i*id
        
    print(res)
        
if __name__ == '__main__':
    main()