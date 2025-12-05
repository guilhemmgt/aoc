#
#   Idea:
#   same thing as part 1, but with a bit of mental gymnastics to generalize to any number of digits
#

JOLTAGE_NB_DIGITS = 12

with open('input') as f:
    input = f.readlines()

sum = 0
for line in input:
    line = line.strip()
    digits_idxs = [i for i in range(0, JOLTAGE_NB_DIGITS)]
    for i in range(0, len(line)):
        for d in range(0, JOLTAGE_NB_DIGITS):  # d: the position of the digit in the joltage
            digit_idx = digits_idxs[d] # digit_idx: the idx of the digit in the line
            digit = int(line[digit_idx])  # digit: the actual digit
            if i < len(line) - (JOLTAGE_NB_DIGITS - d - 1) and int(line[i]) > digit and not i in digits_idxs[:d]:
                # sets the dth joltage digit = to the ith line digit
                for n in range(0, JOLTAGE_NB_DIGITS - d):
                    digits_idxs[d + n] = i + n
    digit = int("".join(line[i] for i in digits_idxs))
    sum += digit

print(sum)
