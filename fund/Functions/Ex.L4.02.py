n1 = int(input())
n2 = int(input())
n3 = int(input())


def solve(n1, n2, n3):
    sum = 0
    sum += n1 + n2
    sum -= n3
    return sum


print(solve(n1, n2, n3))
