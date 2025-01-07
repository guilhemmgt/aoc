# slow af bruteforce

def is_design_possible(requested, availables):
    current = [requested]
    ok = False
    while len(current) > 0:
        next = []
        for c_pattern in current:
            for a_pattern in availables:
                if c_pattern == a_pattern:
                    ok = True
                    break
                elif c_pattern.startswith(a_pattern):
                    next.append(c_pattern[len(a_pattern):])
            if ok: break
        if ok: break
        current = next
    return ok

def main():
    with open('input') as f:
        input = f.readlines()
    
    # avaible towel patterns
    available = input[0].replace("\n", "").split(', ')
    # requested patterns
    requested = [input[i].replace("\n", "") for i in range(2, len(input))]
    
    # a lot of available patterns can be recreated using other available patterns. we get rid of those
    available = [p for p in available if not is_design_possible(p, [p_ for p_ in available if p != p_])]
    
    # compute
    res = 0
    for r_pattern in requested:
        if is_design_possible(r_pattern, available):
            res += 1
            
    print(res)
    
if __name__ == '__main__':
    main()