import re

def testIfStartsWithNumber (str):
    if str.startswith ('one') or str.startswith ('1'):
        return '1'
    if str.startswith ('two') or str.startswith ('2'):
        return '2'
    if str.startswith ('three') or str.startswith ('3'):
        return '3'
    if str.startswith ('four') or str.startswith ('4'):
        return '4'
    if str.startswith ('five') or str.startswith ('5'):
        return '5'
    if str.startswith ('six') or str.startswith ('6'):
        return '6'
    if str.startswith ('seven') or str.startswith ('7'):
        return '7'
    if str.startswith ('eight') or str.startswith ('8'):
        return '8'
    if str.startswith ('nine') or str.startswith ('9'):
        return '9'
    if str.startswith ('zero') or str.startswith ('0'):
        return '0'
    return None

with open('input') as f:
    input = f.readlines()

sum = 0
for line in input:
    first = None
    last = None
    for i in range(0, len(line)):
        n = testIfStartsWithNumber(line[i:])
        if n != None:
            if first == None:
                first = n
            last = n
    sum += (int)(first + last)

print(sum)
