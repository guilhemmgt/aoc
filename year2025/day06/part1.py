import re


def get_function(op):
    match op:
        case '+': return lambda a, b: a + b
        case '*': return lambda a, b: a * b
        case _: raise Exception(f"Unknown operand {op}")


def get_neutral(op):
    match op:
        case '+': return 0
        case '*': return 1
        case _: raise Exception(f"Unknown operand {op}")


def main():
    with open('input') as f:
        input = [line.strip() for line in f]

    numbers = [[int(x) for x in re.findall(r'\d+', l)] for l in input[:-1]]
    operands = re.findall(f'[*+]', input[-1])

    grand_total = 0
    for col in range(0, len(operands)):
        op = operands[col]
        line_res = get_neutral(op)
        for row in range(0, len(numbers)):
            line_res = get_function(op)(line_res, numbers[row][col])
        grand_total += line_res

    print(grand_total)


if __name__ == '__main__':
    main()
