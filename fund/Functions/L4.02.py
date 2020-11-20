operator = input()
n1 = int(input())
n2 = int(input())


def solve(n1, n2, operator):
    if operator == "multiply":
        return n1 * n2
    elif operator == "divide":
        return n1 // n2
    elif operator == "add":
        return n1 + n2
    elif operator == "subtract":
        return n1 - n2


print(solve(n1, n2, operator))