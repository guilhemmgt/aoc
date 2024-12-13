def getFirstFree():
    global firstFree
    for i in range(0 if firstFree == None else firstFree, len(memory)):
        id = memory[i]
        if id == None:
            firstFree = i
            return i
    return None

def free(i):
    allocate(i, None)
def allocate(i, id):
    memory[i] = id

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
    global firstFree; firstFree = None
    for i in range(0, len(memory)):
        j = len(memory)-1-i
        id = memory[j]
        if id != None:
            freeIdx = getFirstFree()
            if freeIdx > j: break
            allocate(freeIdx, id)
            free(j)
            
    # checksum
    res = 0
    for i in range(0, len(memory)):
        id = memory[i]
        if id == None: break
        res += i*id
        
    print(res)
        
if __name__ == '__main__':
    main()