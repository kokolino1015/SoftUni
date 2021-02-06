def get_matrix():
    matrix = [[int(x) for x in input().split(" ")] for x in range(int(input()))]
    return matrix


def get_sum(matrix):
    left_sum = 0
    right_sum = 0
    for i in range(len(matrix)):
        left_sum += matrix[i][i]
        right_sum += matrix[i][len(matrix) - 1 - i]
    return (left_sum, right_sum)


def result(data):
    print(abs(data[0] - data[1]))


result(get_sum(get_matrix()))
