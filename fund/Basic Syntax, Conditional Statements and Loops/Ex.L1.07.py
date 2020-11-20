divisor = int(input())
bound = int(input())
max_size = 0

for i in range(divisor, bound + 1):
    if max_size < i and i % divisor == 0:
        max_size = i
print(max_size)