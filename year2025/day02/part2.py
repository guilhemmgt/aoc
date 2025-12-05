# fuck it we bruteforce

import re

with open('input') as f:
    input = f.readlines()
input = re.findall(r'\d+', input[0])

sum = 0
for i in range(0, int(len(input) / 2)):
    lb = int(input[i * 2])
    ub = int(input[i * 2 + 1])
    for n in range(lb, ub + 1):
        str_n = str(n)
        len_n = len(str_n)

        for t in range(2, len_n + 1):
            if len_n % t != 0:
                continue
            part_length = len_n // t
            first_part = str_n[:part_length]
            if str_n == first_part * t:
                sum += n
                break

print(sum)
