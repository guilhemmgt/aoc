import re

RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14

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
    legal = True
    
    id = int(re.findall(r'\d+', game)[0])
    
    sets_str = game.split(':')[1].split(';')
    for set_str in sets_str:
        red = getColorFromSet('red', set_str)
        green = getColorFromSet('green', set_str)
        blue = getColorFromSet('blue', set_str)

        if red > RED_MAX or green > GREEN_MAX or blue > BLUE_MAX:
            legal = False
            break
        
    if legal:
        sum += id
        
print(sum)