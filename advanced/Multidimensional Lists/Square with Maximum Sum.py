def get_information():
    (rows, colons) = [int(x) for x in input().split(", ")]
    return (rows, colons)


def get_matrix(data):
    matrix = []
    for i in range(int(data[0])):
        nums = input().split(", ")
        matrix.append([int(x) for x in nums])
    return (matrix, data)


def search(data):
    rows, column = data[1]
    matrix = data[0]
    max_sum = -99999999999999
    place = []
    for i in range(rows - 1):
        for j in range(column - 1):
            current_sum = int(matrix[i][j]) + int(matrix[i][j + 1]) + int(matrix[i + 1][j]) + int(matrix[i + 1][j + 1])
            if max_sum < current_sum:
                max_sum = current_sum
                place = [int(matrix[i][j]), int(matrix[i][j + 1]), int(matrix[i + 1][j]), int(matrix[i + 1][j + 1])]
    print(place[0], place[1])
    print(place[2], place[3])
    print(max_sum)


search(get_matrix(get_information()))
