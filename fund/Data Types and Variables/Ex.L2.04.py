lines = int(input())
sum = 0
for i in range(1, lines + 1):
    s = input()
    sum += ord(s)
print(f"The sum equals: {sum}")