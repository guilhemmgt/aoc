import re

class Context:
    ra=0
    rb=0
    rc=0
    pointer=0
    output = []

def adv(n, ctx):
    ctx.ra = int(ctx.ra/(2**combo(n, ctx)))
    ctx.pointer += 2
    return ctx
def bxl(n, ctx):
    ctx.rb = ctx.rb ^ n
    ctx.pointer += 2
    return ctx
def bst(n, ctx):
    ctx.rb = combo(n, ctx) % 8
    ctx.pointer += 2
    return ctx
def jnz(n, ctx):
    if ctx.ra != 0:
        ctx.pointer = n
    else:
        ctx.pointer += 2
    return ctx
def bxc(n, ctx):
    ctx.rb = ctx.rb ^ ctx.rc
    ctx.pointer += 2
    return ctx
def out(n, ctx):
    ctx.output.append(combo(n, ctx) % 8)
    ctx.pointer += 2
    return ctx
def bdv(n, ctx):
    ctx.rb = int(ctx.ra/(2**combo(n, ctx)))
    ctx.pointer += 2
    return ctx
def cdv(n, ctx):
    ctx.rc = int(ctx.ra/(2**combo(n, ctx)))
    ctx.pointer += 2
    return ctx

def combo(n, ctx):
    match(n):
        case 0 | 1 | 2 | 3: return n
        case 4: return ctx.ra
        case 5: return ctx.rb
        case 6: return ctx.rc
        case _: print('invalid combo value', n)

def main():
    with open('input') as f:
        input = f.read()
    parsed_input = [int(x) for x in re.findall(r'\d+', input)]
    
    program = parsed_input[3:]
    
    ctx = Context()
    ctx.ra = parsed_input[0]
    ctx.rb = parsed_input[1]
    ctx.rc = parsed_input[2]
    ctx.pointer = 0
    ctx.output = []
    
    while ctx.pointer < len(program)-1:
        opcode = program[ctx.pointer]
        operand = program[ctx.pointer+1]

        match opcode:
            case 0: ctx = adv(operand, ctx)
            case 1: ctx = bxl(operand, ctx)
            case 2: ctx = bst(operand, ctx)
            case 3: ctx = jnz(operand, ctx)
            case 4: ctx = bxc(operand, ctx)
            case 5: ctx = out(operand, ctx)
            case 6: ctx = bdv(operand, ctx)
            case 7: ctx = cdv(operand, ctx)

    res = ""
    for n in ctx.output:
        res += str(n) + ','
    res = res[:-1]
        
    print(res)
    
if __name__ == '__main__':
    main()