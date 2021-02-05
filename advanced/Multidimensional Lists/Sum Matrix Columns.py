def get_information():
    (rows, colons) = [int(x) for x in input().split(", ")]
    return (rows, colons)


def get_matrix(data):
    matrix = []
    for i in range(int(data[0])):
        nums = input().split(" ")
        matrix.append([int(x) for x in nums])
    return (matrix, data[0], data[1])


def line_summing(data):
    matrix = data[0]
    rows = data[1]
    colons = data[2]
    for i in range(colons):
        summing = 0
        for j in range(rows):
            summing += matrix[j][i]
        print(summing)


line_summing(get_matrix(get_information()))
