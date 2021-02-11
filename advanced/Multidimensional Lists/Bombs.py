def is_valid(row, col, size):
    return 0 <= row < size and 0 <= col < size


def destroy(bomb, matrix):
    rows = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    cols = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    detonate = matrix[bomb[0]][bomb[1]]
    if detonate <= 0:
        return matrix
    for x in range(9):
        current_position = [bomb[0] + rows[x], bomb[1] + cols[x]]
        if is_valid(current_position[0], current_position[1], len(matrix)) and matrix[current_position[0]][
            current_position[1]] > 0:
            matrix[current_position[0]][current_position[1]] -= detonate
    return matrix


def get_matrix(n):
    matrix = [[int(x) for x in input().split(" ")] for _ in range(n)]
    return matrix


def bombs_coordinates():
    bombs = [x for x in input().split(" ")]
    return bombs


def solve(matrix, bombs):
    for i in bombs:
        current_row, current_col = [int(x) for x in i.split(",")]
        bomb = [current_row, current_col]
        matrix = destroy(bomb, matrix)
    return matrix


def result(matrix):
    total = 0
    alive = 0
    for i in matrix:
        for j in i:
            if j > 0:
                total += j
                alive += 1
    print(f"Alive cells: {alive}")
    print(f"Sum: {total}")
    for i in matrix:
        i = [str(x) for x in i]
        print(" ".join(i))


result(solve(get_matrix(int(input())), bombs_coordinates()))
