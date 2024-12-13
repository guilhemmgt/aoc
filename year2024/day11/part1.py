import re
import sys

def main():
    with open('input') as f:
        input = f.readlines()
    
    stones = [int(x) for x in re.findall(r'\d+', ''.join(input))]

    for blink in range(0, 25):
        new_stones = []
        for stone in stones:
            if stone == 0: # rule 1
                new_stones.append(1)
            else: 
                str_stone = str(stone)
                len_stone = len(str_stone)
                if len_stone % 2 == 0: # rule 2
                    new_stones.append(int(str_stone[:int(len_stone/2)]))
                    new_stones.append(int(str_stone[int(len_stone/2):]))
                else: # rule 3
                    new_stones.append(stone*2024)
        stones = new_stones
        
    print(len(stones))
        
if __name__ == '__main__':
    main()