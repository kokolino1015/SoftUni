numbers = input().split(" ")
numbers = [int(x) for x in numbers]
sum_of_numbers = 0
for i in numbers:
    sum_of_numbers += i
avr_sum = sum_of_numbers / len(numbers)
bigger_nums = []
for i in numbers:
    if avr_sum < float(i):
        bigger_nums.append(i)

bigger_nums.sort(reverse=True)

if len(bigger_nums) <= 5:
    if len(bigger_nums) > 0:
        bigger_nums = [str(x) for x in bigger_nums]
        print(" ".join(bigger_nums))
    else:
        print("No")
elif len(bigger_nums) > 5:
    removing = len(bigger_nums) - 5
    while removing > 0:
        bigger_nums.pop(-1)
        removing -= 1
    bigger_nums = [str(x) for x in bigger_nums]
    print(" ".join(bigger_nums))