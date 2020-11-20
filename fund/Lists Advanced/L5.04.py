numbers = input().split(", ")
list = []

for i in range(len(numbers)):
    if int(numbers[i]) % 2 == 0:
        list.append(i)

print(list)