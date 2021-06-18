num = int(input())

list = []
for i in range(1, num+1):
    list.append(i)
    print(' '.join(str(j) for j in list))
for j in range(1, num+1):
    list.pop()
    print(' '.join(str(j) for j in list))
