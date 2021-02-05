rows, colons = input().split(", ")
matrix = []
summing = 0

for i in range(int(rows)):
    nums = input().split(", ")
    matrix.append([int(x) for x in nums])

for i in matrix:
    summing += sum(i)
print(summing)
print(matrix)
