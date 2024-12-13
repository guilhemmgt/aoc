import re
import sys

BLINKS = 75

def process_stone(stone):
    if stone == 0: # rule 1
        return [1]
    else:
        str_stone = str(stone)
        len_stone = len(str_stone)
        if len_stone % 2 == 0: # rule 2
            return [int(str_stone[:len_stone//2]), int(str_stone[len_stone//2:])]
        else: # rule 3
            return [stone*2024]

def main():
    # read file
    with open('input') as f:
        input = f.readlines()
        
    # parse & init
    current_stones = {}
    for x in re.findall(r'\d+', ''.join(input)):
        x = int(x)
        if x in current_stones:
            current_stones[x] += 1
        else:
            current_stones[x] = 1
        
    # compute
    for blink in range(0, BLINKS):
        new_stones = {}
        for stone in current_stones:
            count = current_stones[stone]
            resulting_stones = process_stone(stone)
            for res_s in resulting_stones:
                if res_s in new_stones:
                    new_stones[res_s] += count
                else:
                    new_stones[res_s] = count
        current_stones = new_stones
        
    print(sum([current_stones[k] for k in current_stones]))
        
if __name__ == '__main__':
    main()