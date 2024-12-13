import re

with open('input') as f:
    input = f.readlines()
    
sum = 0
    
for card in input:
    content = card.split(':')[1].split('|')
    winning = re.findall(r'\d+', content[0])
    have = re.findall(r'\d+', content[1])
    
    points = 0
    
    for n in have:
        if n in winning:
            points = 1 if points == 0 else points*2
    
    sum += points
    
print(sum)
