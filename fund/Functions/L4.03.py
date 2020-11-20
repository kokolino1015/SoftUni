string = input()
times = int(input())


def solve(string, times):
    result = ""
    for i in range(times):
        result += string
    return result


print(solve(string, times))
