def solve(n):
    res = set()
    for i in range(n):
        token = input().split(" ")
        for j in token:
            res.add(j)
    return res


def result(res):
    for i in res:
        print(i)


result(solve(int(input())))
