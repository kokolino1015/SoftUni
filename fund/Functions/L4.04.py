name = input()
times = int(input())


def solve(name, times):
    result = 0
    if name == "water":
        result += times * 1.00
    elif name == "coffee":
        result += times * 1.50
    elif name == "coke":
        result += times * 1.40
    elif name == "snacks":
        result += times * 2.00
    return result


print(f"{solve(name, times):.2f}")