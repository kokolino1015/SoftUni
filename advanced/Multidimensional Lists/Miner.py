def search_position(position, matrix):
    symbol = matrix[position[0]][position[1]]
    return symbol


def is_valid(position, size):
    return 0 <= position[0] < size and 0 <= position[1] < size


def search_for_coals(matrix):
    coals = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == "c":
                coals += 1
    return coals


def find_start(matrix):
    s_position = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == "s":
                s_position = [i, j]
                return s_position


def get_input(n):
    commands = input().split(" ")
    matrix = [[x for x in input().split(" ")] for _ in range(n)]
    return (matrix, commands)


def solve(data):
    matrix = data[0]
    commands = data[1]
    row_miner, col_miner = find_start(matrix)
    current_position = [row_miner, col_miner]
    for i in commands:
        if search_for_coals(matrix) == 0:
            print(f"You collected all coals! ({current_position[0]}, {current_position[1]})")
            return
        if i == "up":
            if is_valid([current_position[0] - 1, current_position[1]], len(matrix)):
                symbol = search_position([current_position[0] - 1, current_position[1]], matrix)
                current_position = [current_position[0] - 1, current_position[1]]
                if symbol == "c":
                    matrix[current_position[0]][current_position[1]] = "*"
                elif symbol == "e":
                    print(f"Game over! ({current_position[0]}, {current_position[1]})")
                    return
        elif i == "down":
            if is_valid([current_position[0] + 1, current_position[1]], len(matrix)):
                symbol = search_position([current_position[0] + 1, current_position[1]], matrix)
                current_position = [current_position[0] + 1, current_position[1]]
                if symbol == "c":
                    matrix[current_position[0]][current_position[1]] = "*"
                elif symbol == "e":
                    print(f"Game over! ({current_position[0]}, {current_position[1]})")
                    return
        elif i == "left":
            if is_valid([current_position[0], current_position[1] - 1], len(matrix)):
                symbol = search_position([current_position[0], current_position[1] - 1], matrix)
                current_position = [current_position[0], current_position[1] - 1]
                if symbol == "c":
                    matrix[current_position[0]][current_position[1]] = "*"
                elif symbol == "e":
                    print(f"Game over! ({current_position[0]}, {current_position[1]})")
                    return
        elif i == "right":
            if is_valid([current_position[0], current_position[1] + 1], len(matrix)):
                symbol = search_position([current_position[0], current_position[1] + 1], matrix)
                current_position = [current_position[0], current_position[1] + 1]
                if symbol == "c":
                    matrix[current_position[0]][current_position[1]] = "*"
                elif symbol == "e":
                    print(f"Game over! ({current_position[0]}, {current_position[1]})")
                    return
    if search_for_coals(matrix) == 0:
        print(f"You collected all coals! ({current_position[0]}, {current_position[1]})")
        return
    else:
        print(f"{search_for_coals(matrix)} coals left. ({current_position[0]}, {current_position[1]})")


solve(get_input(int(input())))
