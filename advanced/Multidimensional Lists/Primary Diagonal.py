def get_input():
    num = int(input())
    matrix = []
    for i in range(num):
        matrix.append([int(x) for x in input().split(" ")])
    return (num, matrix)


def result(data):
    summing = 0
    for i in range(data[0]):
        summing += data[1][i][i]
    print(summing)


result(get_input())
