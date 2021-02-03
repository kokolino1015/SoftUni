def solve(word):
    line = tuple(ch for ch in word)
    symbols = {}
    for i in line:
        if i not in symbols:
            symbols[i] = 0
        symbols[i] += 1
    return symbols


def print_result(res):
    symbol = sorted(res.items(), key=lambda x: (x[0]))
    for r in symbol:
        print(f"{r[0]}: {r[1]} time/s")


print_result(solve(input()))
