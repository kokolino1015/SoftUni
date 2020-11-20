n = input()
beg = int(input())
list_2 = n.split(", ")
numbers = []

for i in list_2:
    d = int(i)
    numbers.append(d)

h1 = []

for i in range(beg):
    h1.append(0)

index = 0

for i in numbers:
    h1[index] += i
    index += 1
    if index == beg:
        index = 0

print(h1)