from functools import reduce


def operate(operator, *nums):
    return reduce(lambda x, y: eval(f"{x} {operator} {y}"), nums)
