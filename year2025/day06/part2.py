def get_function(op):
    match op:
        case '+': return lambda a, b: a + b
        case '*': return lambda a, b: a * b
        case _: raise Exception(f"Unknown op {op}")


def get_neutral(op):
    match op:
        case '+': return 0
        case '*': return 1
        case _: raise Exception(f"Unknown op {op}")


def main():
    with open('input') as f:
        input = [line.strip('\n') for line in f]

    numbers = input[:-1]
    operands = input[-1] + " " # add extra space bc it makes parsing easier dont worry about it

    grand_total = 0
    
    cursor = 0 # the "start" of the current problem (also = the index of its operand char in 'operands')
    while cursor < len(operands):
        op = operands[cursor]

        # computes the "length" of the problem: the nb of chars it occupies (also = the nb of chars from the problem's operand to the next's)
        problem_length = 0
        while cursor + problem_length + 1 < len(operands) and operands[cursor + problem_length + 1] not in ['+', '*']:
            problem_length += 1

        # read each number of the problem, and computes its answer
        problem_res = get_neutral(op)
        for col in range(cursor, cursor + problem_length):
            num = int(''.join(numbers[row][col] for row in range(0, len(numbers))))
            problem_res = get_function(op)(problem_res, num)

        grand_total += problem_res

        # move to the next problem !
        cursor += problem_length + 1

    print(grand_total)


if __name__ == '__main__':
    main()
