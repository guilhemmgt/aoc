with open('input') as f:
    input = f.readlines()

times_at_zero = 0
dial = 50

for instr in input:
    dial = (dial + ((instr[0] == 'R') * 2 - 1) * int(instr[1:])) % 100
    times_at_zero += dial == 0

print(times_at_zero)
