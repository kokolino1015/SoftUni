n1 = int(input())
n2 = int(input())
sum = n1 * n2
list = []

for i in range(n1, sum + 1, n1):
    list.append(i)

print(list)