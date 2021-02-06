def get_matrix():
    rows, columns = input().split(" ")
    matrix = [[int(x) for x in input().split()] for x in range(int(rows))]
    return (matrix, rows, columns)


def searching(data):
    matrix = data[0]
    rows = int(data[1])
    column = int(data[2])
    maximum = -9999999
    for i in range(rows - 2):
        for j in range(column - 2):
            line1 = [matrix[i][j], matrix[i][j + 1], matrix[i][j + 2]]
            line2 = [matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2]]
            line3 = [matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]]
            total = sum(line1) + sum(line2) + sum(line3)

            if total > maximum:
                maximum = total
                best_line1 = line1
                best_line2 = line2
                best_line3 = line3

    print(f"Sum = {maximum}")
    print(" ".join(map(str, best_line1)))
    print(" ".join(map(str, best_line2)))
    print(" ".join(map(str, best_line3)))



searching(get_matrix())
