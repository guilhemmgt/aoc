#
#   Idea :
#   All invalid IDs can be written as 'nn' where n is a positive integer.
#   For each interval I, we will get every n such that 'nn' is in I.
#

import re


def double(n):
    """
    Returns `n` repeated twice, e.g. double(12) = 1212.
    """
    return int(str(n) * 2)


with open('input') as f:
    input = f.readlines()
input = re.findall(r'\d+', input[0])

sum = 0
for i in range(0, int(len(input) / 2)):
    lb = int(input[i * 2])  # input lower bound
    ub = int(input[i * 2 + 1])  # input upper bound
    lb_len = len(str(lb))  # nb of chars in the lower bound

    # decides the first value of n
    if lb_len % 2 != 0:
        # lb=222220 => n=222 (first half of lb)
        n = int(str(lb)[0:int(lb_len / 2)])
        # beware: lb=565653 => n=566, not 565 (because 565565 < lb and we need lb < 'nn')
        if double(n) < lb:
            n += 1
    else:
        # lb=998 => n=10 (first half of the next integer with an even nb of chars, 1000)
        n = int('1' + '0' * int((lb_len - 1) / 2))

    # checks all n in the interval and sums their corresponding 'nn'
    while double(n) <= ub:
        sum += double(n)
        n += 1

print(sum)
