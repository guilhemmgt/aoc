#
#   Idea:
#   for each line,
#   the 1st digit of the largest joltage is the highest digit in line[:len(line) - 1]
#   the 2nd digit is the highest digit in line[first_digit_idx + 1:]
#   + we can do that in 1 loop
#

with open('input') as f:
    input = f.readlines()

sum = 0
for line in input:
    line = line.strip()
    first_digit_idx = 0
    second_digit_idx = 1
    for i in range(0, len(line)):
        if i < len(line) - 1 and line[i] > line[first_digit_idx]:
            first_digit_idx = i
            second_digit_idx = i + 1
        elif i != first_digit_idx and line[i] >= line[second_digit_idx]:
            second_digit_idx = i
    digit = int(str(line[first_digit_idx]) + str(line[second_digit_idx]))
    sum += digit

print(sum)
