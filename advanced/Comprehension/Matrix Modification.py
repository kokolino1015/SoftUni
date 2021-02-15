def is_valid(row, col, size):
    return 0 <= row < size and 0 <= col < size


def get_matrix(n):
    matrix = [[int(x) for x in input().split(" ")] for _ in range(n)]
    return (matrix, n)


def solve(data):
    matrix = data[0]
    command = input().split(" ")
    while "END" not in command:
        action = command[0]
        row = int(command[1])
        col = int(command[2])
        num = int(command[3])
        if is_valid(row, col, data[1]):
            if action == "Subtract":
                matrix[row][col] -= num
            elif action == "Add":
                matrix[row][col] += num
        else:
            print("Invalid coordinates")
        command = input().split(" ")
    return matrix


def print_matrix(matrix):
    print(*[" ".join(str(x) for x in row) for row in matrix], sep="\n")


print_matrix(solve(get_matrix(int(input()))))
