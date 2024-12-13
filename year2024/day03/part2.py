import re 

with open('input') as f:
    input = f.readlines()

input_str = ''.join(input)
    
instructions = re.findall(r'mul\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\)|do\(\)|don\'t\(\)', input_str)

do = True
sum = 0
for instr in instructions:
    if instr == 'do()':
        do = True
    elif instr == 'don\'t()':
        do = False
    elif do:
        numbers = re.findall(r'\d+', instr)
        sum += int(numbers[0]) * int(numbers[1])

print (sum)