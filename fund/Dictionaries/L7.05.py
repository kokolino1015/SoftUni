times = int(input())
dictionary = {}
index = 1

for i in range(1, times + 1):
    key = input()
    value = input()
    if key not in dictionary:
        dictionary[key] = []
    dictionary[key].append(value)

for i in dictionary:
    print(f"{i} - {', '.join(dictionary[i])}")