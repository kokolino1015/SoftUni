def solve():
    matrix = input().split('|')
    matrix.reverse()
    result = [value.strip() for i in range(len(matrix)) for value in matrix[i].split()]
    print(*result)


solve()
