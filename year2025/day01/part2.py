with open('input') as f:
    input = f.readlines()

times_at_zero = 0
dial = 50

for instr in input:
    temp_dial = dial + ((instr[0] == 'R') * 2 - 1) * int(instr[1:])
    times_at_zero += (temp_dial == 0) + (abs(temp_dial) // 100) + (temp_dial * dial < 0)
    dial = temp_dial % 100

print(times_at_zero)
