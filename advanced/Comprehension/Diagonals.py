def solve(n):
    matrix = [[int(x) for x in input().split(", ")] for _ in range(n)]
    print(
        f"First diagonal: {', '.join(str(matrix[i][i]) for i in range(n))}. Sum: {sum(matrix[i][i] for i in range(n))}")
    print(
        f"Second diagonal: {', '.join(str(matrix[i][n - 1 - i]) for i in range(n))}. Sum: {sum(matrix[i][n - 1 - i] for i in range(n - 1, -1, -1))}")


solve(int(input()))
