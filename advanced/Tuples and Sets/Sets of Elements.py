def input_lines(n):
    res = set()
    for _ in range(n):
        res.add(input())
    return res


def intersection(a, b):
    return a.intersection(b)


def result(res):
    for r in res:
        print(r)


len1, len2 = input().split(" ")
line1 = input_lines(int(len1))
lene2 = input_lines(int(len2))
result(intersection(line1, lene2))
