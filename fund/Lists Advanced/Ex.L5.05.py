num = int(input())
res = []
index = 1
while 0 < num:
    value = 2 * index ** 2
    if value > num:
        res.append(num)
        break
    res.append(value)
    num -= value
    index += 1
print(res)