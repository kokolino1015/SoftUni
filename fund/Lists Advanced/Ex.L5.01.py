list = input().split(", ")
list2 = input().split(", ")
list3 = []

for i in list:
    for j in list2:
        if i in j:
            list3.append(i)
            break

print(list3)
