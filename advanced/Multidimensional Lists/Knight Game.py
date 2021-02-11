def is_valid(pos, size):
    return 0 <= pos[0] < size and 0 <= pos[1] < size


def kills(current_row, current_col, board, row):
    cols = [-2, -2, -1, 1, 2, 2, -1, 1]
    rows = [1, -1, 2, 2, 1, -1, -2, -2]
    kill = 0
    position = [current_row, current_col]
    for i in range(8):
        current_pos = [current_row + rows[i], current_col + cols[i]]
        if is_valid(current_pos, row) and board[current_pos[0]][current_pos[1]] == "K":
            kill += 1
    return (kill, board, position)


def get_table(row_col):
    matrix = []
    for i in range(row_col):
        row = input()
        row = " ".join(row)
        matrix.append(row.split(" "))
    return (matrix, row_col)


def search(data):
    matrix = data[0]
    row = data[1]
    col = data[1]
    total_kills = 0
    while True:
        best_killer = 0
        monster = []
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == "K":
                    get_kills, matrix, pos = kills(i, j, matrix, row)
                    if get_kills > best_killer:
                        best_killer = get_kills
                        monster = [pos[0], pos[1]]
        if monster:
            total_kills += 1
            matrix[monster[0]][monster[1]] = 0
        else:
            break

    print(total_kills)


search(get_table(int(input())))
