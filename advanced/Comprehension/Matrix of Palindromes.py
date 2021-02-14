def solve():
    row, cols = [int(x) for x in input().split(" ")]
    matrix = [[f"{chr(97 + i)}{chr(97 + i + j)}{chr(97 + i)}" for j in range(cols)] for i in range(row)]
    print(*[" ".join(x) for x in matrix], sep="\n")


solve()
