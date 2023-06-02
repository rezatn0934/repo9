import operator


def calculator(Number1, Op, Number2):
    if Op == '+':
        return operator.add(Number1, Number2)
    if Op == '-':
        return operator.add(Number1, Number2)
    elif Op == '/':
        return Number1 / Number2
    elif Op == '*':
        return operator.mul(Number1, Number2)
    else:
        raise TypeError
