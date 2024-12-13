import re

def isSymbol (str):
    return re.match(r'[^0-9.\n]', str) != None

with open('input') as f:
    input = f.readlines()
    
chars = [c for c in input]

width = len(input[0])
height = len(input)

sum = 0

for l in range(0,len(chars)):
    line = chars[l]
    c = 0
    while c < len(line):
        subline = line[c:]
        match = re.findall(r'^\d+', subline)
        
        # we retrieved a number
        if match != []:
            n_str = match[0]
            n_len = len(n_str)
            n_int = int(n_str)
            
            legal = False
            
            # check if a gear is near the number (<=> the number is "legal")
            if (c > 0) and isSymbol(line[c-1]): legal = True # before n
            if (c + n_len < width-1) and isSymbol(line[c+n_len]): legal = True # after n
            if (l > 0): 
                for i in range(c, c+n_len):
                    if isSymbol(chars[l-1][i]): legal = True # above n
                if (c > 0) and isSymbol(chars[l-1][c-1]): legal = True # before (above n)
                if (c + n_len < width-1) and isSymbol(chars[l-1][c+n_len]): legal = True # after (above n)
            if (l < height-1): 
                for i in range(c, c+n_len):
                    if isSymbol(chars[l+1][i]): legal = True # under n
                if (c > 0) and isSymbol(chars[l+1][c-1]): legal = True # before (under n)
                if (c + n_len < width-1) and isSymbol(chars[l+1][c+n_len]): legal = True # after (under n)
                
            # if a gear is nearby, add n to the sum
            if legal:
                sum += n_int
                
            c += n_len # if n=256, do not process 56 and 6
                
        c += 1
            
print(sum)