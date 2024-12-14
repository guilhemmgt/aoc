import re

def main():
    with open('input') as f:
        input = f.readlines()
    input = ''.join(input)
    
    # machines = array of [Ax, Ay, Bx, By, Px, Py]
    machines = [ [int(x) for x in re.findall(r'\d+', machine_str)] for machine_str in input.split('\n\n')]
    
    tokens = 0
    for machine in machines:
        ax, ay, bx, by, px, py = machine
        px += 10000000000000
        py += 10000000000000
        # math (only 1 solution)
        b = (py/ay-px/ax) * 1 / (by/ay-bx/ax)
        a = (px-b*bx)/ax
        # checks if solution is in N²
        if abs(a-round(a)) < 0.001 and abs(b-round(b)) < 0.001:
            tokens += 3*round(a)+round(b)
        
    print(tokens)
        
if __name__ == '__main__':
    main()