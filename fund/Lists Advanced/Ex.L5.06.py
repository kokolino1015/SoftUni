import math

list_str_num = input().split(", ")
list_str_num = [int(x) for x in list_str_num]
max_num = max(list_str_num)
lists = math.ceil(max_num / 10)

for i in range(1, lists + 1):
    current_list = []
    for j in list_str_num:
        upper = i * 10
        lower = upper - 10
        if lower < j <= upper:
            current_list.append(j)
    print(f"Group of {i * 10}'s: {current_list}")
