from functools import reduce


def operate(operator, *nums):
    mapper = {
        '-': lambda x, y: x - y,
        '/': lambda x, y: x / y,
        '*': lambda x, y: x * y,
        '+': lambda x, y: x + y
    }
    return reduce(mapper[operator], nums)
