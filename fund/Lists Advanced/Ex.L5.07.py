def one(word):
    num = ""
    for i in word:
        if not str(i).isdigit():
            break
        num += i
    s = int(num)
    d = chr(s)
    new_word = word.replace(num, d)
    return new_word


def two(word):
    temp = list(word)
    temp[1], temp[-1] = temp[-1], temp[1]
    return "".join(temp)


def solve(word):
    res = one(word)
    res = two(res)
    return res


words = input().split(" ")
new_word = [solve(word) for word in words]

print(" ".join(new_word))
