line = input().split(" ")

result = ""
for i in line:
    value = len(i)
    for j in range(value):
        result += i

print(result)