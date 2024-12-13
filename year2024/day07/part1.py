import re

def mult(list):
    return [list[0]*list[1]] + list[2:]
def plus(list):
    return [list[0]+list[1]] + list[2:]

def compute(target, numbers):
    if len(numbers)==1:
        return numbers[0] == target
    else:
        return compute(target, mult(numbers)) or compute(target, plus(numbers))

def main():
    with open('input') as f:
        input = f.readlines()
        
    res = 0
    for l in input:
        target = int(l.split(':')[0])
        numbers = [int(x) for x in re.findall(r'\d+', l.split(':')[1])]
        if compute(target, numbers):
            res += target
            
    print(res)
        
if __name__ == '__main__':
    main()