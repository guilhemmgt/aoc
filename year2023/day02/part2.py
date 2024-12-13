import re

def getColorFromSet(color_name, set_str):
    match = re.compile(r'(\d+) ' + color_name).search(set_str)
    if match == None:
        return 0
    else:
        return int(match.group(1))

with open('input') as f:
    input = f.readlines()
    
sum = 0
    
for game in input:
    min_red = 0
    min_green = 0
    min_blue = 0
    
    sets_str = game.split(':')[1].split(';')
    for set_str in sets_str:
        min_red = max(min_red, getColorFromSet('red', set_str))
        min_green = max(min_green, getColorFromSet('green', set_str))
        min_blue = max(min_blue, getColorFromSet('blue', set_str))

    sum += min_red * min_green * min_blue
    
print(sum)