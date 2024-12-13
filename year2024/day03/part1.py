import re 

with open('input') as f:
    input = f.readlines()

input_str = ''.join(input)
    
instructions = re.findall(r'mul\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\)', input_str)

sum = 0
for instr in instructions:
    numbers = re.findall(r'\d+', instr)
    sum += int(numbers[0]) * int(numbers[1])

print (sum)