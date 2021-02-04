def get_names(n):
    odd = set()
    even = set()
    for i in range(1, n + 1):
        name = input()
        letters = sum([ord(el) for el in name]) // i
        if letters % 2 != 0:
            odd.add(letters)
        else:
            even.add(letters)
    return even,odd


def search(data):
    sum_evens = sum(data[0])
    sum_odds = sum(data[1])
    if sum_evens == sum_odds:
        res = data[0].union(data[1])
        return res
    elif sum_evens < sum_odds:
        res = data[1].difference(data[0])
        return res
    else:
        res = data[0].symmetric_difference(data[1])
        return res


def result(res):
    print(f"{', '.join(str(x) for x in res)}")


result(search(get_names(int(input()))))
