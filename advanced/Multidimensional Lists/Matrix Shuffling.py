def get_matrix():
    rows, columns = [int(x) for x in input().split()]
    matrix = [[x for x in input().split()] for _ in range(int(rows))]
    return (matrix, rows, columns)


def searching(data):
    matrix = data[0]
    rows = int(data[1])
    column = int(data[2])
    command = input()
    while command != "END":
        token = command.split(" ")
        if token[0] == "swap" and len(token) == 5:
            row1 = int(token[1])
            col1 = int(token[2])
            row2 = int(token[3])
            col2 = int(token[4])
            if row1 in range(rows) and row2 in range(rows) and col1 in range(
                column) and col2 in range(column):
                matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
                for i in range(rows):
                    roww = ""
                    for j in range(column):
                        roww += f"{matrix[i][j]} "
                    print(roww)
            else:
                print("Invalid input!")
        else:
            print("Invalid input!")
        command = input()


searching(get_matrix())
