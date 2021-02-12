def bunnies_multiplier(i, j, matrix, row, col):
    board = matrix
    row_pos = [-1, 1, 0, 0]
    col_pos = [0, 0, -1, 1]
    for x in range(4):
        current_position = [i + row_pos[x], j + col_pos[x]]
        if 0 <= current_position[0] < row and 0 <= current_position[1] < col:
            if matrix[current_position[0]][current_position[1]] == "P":
                matrix[current_position[0]][current_position[1]] = "B"
                print("\n".join("".join(map(str, x)) for x in matrix))
                print(f"dead: {current_position[0]} {current_position[1]}")
            elif matrix[current_position[0]][current_position[1]] == ".":
                board[current_position[0]][current_position[1]] = "B"
    return board


def search_for_bunnies(row, col, matrix):
    bunny_positions = []
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == "B":
                bunny_positions.append([i, j])
    for i in bunny_positions:
        matrix = bunnies_multiplier(i[0], i[1], matrix, row, col)
    return matrix


def is_valid(position, row, col):
    return 0 <= position[0] < row and 0 <= position[1] < col


def locate_player(row, col, matrix):
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == "P":
                return [i, j]


def get_input(row_col):
    row, col = [int(x) for x in row_col.split(" ")]
    matrix = [[x for x in input()] for _ in range(row)]
    position = [x for x in input()]
    return (row, col, matrix, position)


def solve(data):
    row = data[0]
    col = data[1]
    matrix = data[2]
    positions = data[3]
    player_position = locate_player(row, col, matrix)
    for i in positions:
        if i == "L":
            current_player_position = [player_position[0], player_position[1] - 1]
            if is_valid(current_player_position, row, col):
                if matrix[current_player_position[0]][current_player_position[1]] == "B":
                    matrix[player_position[0]][player_position[1]] = "."
                    matrix = search_for_bunnies(row, col, matrix)
                    print("\n".join("".join(map(str, x)) for x in matrix))
                    print(f"dead: {current_player_position[0]} {current_player_position[1]}")
                    return
                matrix[player_position[0]][player_position[1]] = "."
                player_position = current_player_position
                matrix[player_position[0]][player_position[1]] = "P"
            elif not is_valid(current_player_position, row, col):
                matrix[player_position[0]][player_position[1]] = "."
                matrix = search_for_bunnies(row, col, matrix)
                print("\n".join("".join(map(str, x)) for x in matrix))
                print(f"won: {player_position[0]} {player_position[1]}")
                return
        elif i == "R":
            current_player_position = [player_position[0], player_position[1] + 1]
            if is_valid(current_player_position, row, col):
                if matrix[current_player_position[0]][current_player_position[1]] == "B":
                    matrix[player_position[0]][player_position[1]] = "."
                    matrix = search_for_bunnies(row, col, matrix)
                    print("\n".join("".join(map(str, x)) for x in matrix))
                    print(f"dead: {current_player_position[0]} {current_player_position[1]}")
                    return
                matrix[player_position[0]][player_position[1]] = "."
                player_position = current_player_position
                matrix[player_position[0]][player_position[1]] = "P"
            elif not is_valid(current_player_position, row, col):
                matrix[player_position[0]][player_position[1]] = "."
                matrix = search_for_bunnies(row, col, matrix)
                print("\n".join("".join(map(str, x)) for x in matrix))
                print(f"won: {player_position[0]} {player_position[1]}")
                return
        elif i == "D":
            current_player_position = [player_position[0] + 1, player_position[1]]
            if is_valid(current_player_position, row, col):
                if matrix[current_player_position[0]][current_player_position[1]] == "B":
                    matrix[player_position[0]][player_position[1]] = "."
                    matrix = search_for_bunnies(row, col, matrix)
                    print("\n".join("".join(map(str, x)) for x in matrix))
                    print(f"dead: {current_player_position[0]} {current_player_position[1]}")
                    return
                matrix[player_position[0]][player_position[1]] = "."
                player_position = current_player_position
                matrix[player_position[0]][player_position[1]] = "P"
            elif not is_valid(current_player_position, row, col):
                matrix[player_position[0]][player_position[1]] = "."
                matrix = search_for_bunnies(row, col, matrix)
                print("\n".join("".join(map(str, x)) for x in matrix))
                print(f"won: {player_position[0]} {player_position[1]}")
                return
        elif i == "U":
            current_player_position = [player_position[0] - 1, player_position[1]]
            if is_valid(current_player_position, row, col):
                if matrix[current_player_position[0]][current_player_position[1]] == "B":
                    matrix[player_position[0]][player_position[1]] = "."
                    matrix = search_for_bunnies(row, col, matrix)
                    print("\n".join("".join(map(str, x)) for x in matrix))
                    print(f"dead: {current_player_position[0]} {current_player_position[1]}")
                    return
                matrix[player_position[0]][player_position[1]] = "."
                player_position = current_player_position
                matrix[player_position[0]][player_position[1]] = "P"
            elif not is_valid(current_player_position, row, col):
                matrix[player_position[0]][player_position[1]] = "."
                matrix = search_for_bunnies(row, col, matrix)
                print("\n".join("".join(map(str, x)) for x in matrix))
                print(f"won: {player_position[0]} {player_position[1]}")
                return
        matrix = search_for_bunnies(row, col, matrix)


solve(get_input(input()))
