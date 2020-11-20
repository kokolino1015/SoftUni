s = int(input())
sum_of_all = 0
max = 255

for i in range(1, s + 1):
    b = int(input())
    if b > max:
        print("Insufficient capacity!")
        continue
    if b + sum_of_all > max:
        print("Insufficient capacity!")
        continue
    elif b + sum_of_all <= max:
        sum_of_all += b

print(sum_of_all)