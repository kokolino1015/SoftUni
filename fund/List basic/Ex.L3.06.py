num = input().split()
remove = int(input())

numbers = []

for i in num:
    numbers.append(int(i))

for i in range(remove):
    max_number = 99999999999
    for f in numbers:
        if f < max_number:
            max_number = f
    numbers.remove(max_number)

print(numbers)