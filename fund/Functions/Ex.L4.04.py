numbers = input()
f = [int(i) for i in numbers]


def solve(f):
    odd = 0
    even = 0
    for j in f:
        if j == 0:
            continue
        elif j % 2 == 0:
            even += j
        elif j % 2 != 0:
            odd += j
    return f"Odd sum = {odd}, Even sum = {even}"


print(solve(f))
