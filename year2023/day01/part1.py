import re

with open('input') as f:
    input = f.readlines()
    
sum = 0
for line in input:
    numbers = re.findall(r'\d', line)
    sum += (int)(numbers[0] + numbers[len(numbers)-1])
    
print(sum)