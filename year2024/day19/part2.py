# still slow

def is_design_possible(design, towels):
    current = {}
    current[design] = 1
    sum = 0
    
    while len(current) > 0:
        next = {}
        for c_design in current:
            for tow in towels:
                if tow == c_design:
                    sum += current[tow]
                elif c_design.startswith(tow):
                    n_design = c_design[len(tow):]
                    if n_design in next:
                        next[n_design] += current[c_design]
                    else:
                        next[n_design] = current[c_design]
        current = next
        
    return sum

def main():
    with open('input') as f:
        input = f.readlines()
    
    # avaible towels
    towels = input[0].replace("\n", "").split(', ')
    # requested designs
    designs = [input[i].replace("\n", "") for i in range(2, len(input))]

    # compute
    res = 0
    for design in designs:
        # removes towels that are not in the design
        new_towels = []
        for t in towels:
            if t in design:
                new_towels.append(t)
        # search
        res += is_design_possible(design, new_towels)
        
    
            
    print(res)
    
if __name__ == '__main__':
    main()