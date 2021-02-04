def getting_information(n):
    data = []
    for i in range(n):
        first, second = input().split("-")
        fs, fe = first.split(",")
        ss, sf = second.split(",")
        fs = int(fs)
        fe = int(fe)
        ss = int(ss)
        sf = int(sf)
        longest_range = range(max(fs, ss), min(fe, sf)+1)
        data.append([el for el in longest_range])
    return data


def result(res):
    res = sorted(res, key=lambda x: -len(x))[0]
    print(f"Longest intersection is {res} with length {len(res)}")


result(getting_information(int(input())))
