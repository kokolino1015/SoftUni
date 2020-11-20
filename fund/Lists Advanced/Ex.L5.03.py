list_string = input().split(".")
first = int(list_string[0])
second = int(list_string[1])
third = int(list_string[2])
third += 1
if third == 10:
    third = 0
    second += 1
    if second == 10:
        second = 0
        first += 1
sun = f"{first}.{second}.{third}"
print(sun)