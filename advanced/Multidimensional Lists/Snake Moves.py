rows, cols = [int(x) for x in input().split()]
string = input()


def get_snake(string, times):
    res = ""
    for i in range(times):
        if i > len(string) - 1:
            while i > len(string) - 1:
                i -= len(string)
        res += string[i]
    return res


def solve(rows, cols, string):
    matrix = []
    res = get_snake(string, (rows * cols))
    index = 0
    for i in range(0, rows):
        matrix.append([])
        for j in range(0, cols):
            if i % 2 == 0:
                matrix[i].append(res[index])
            elif i % 2 != 0:
                matrix[i].insert(0, res[index])
            index += 1
    for i in matrix:
        print("".join(i))


solve(rows, cols, string)
