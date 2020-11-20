words = input().split(" ")
dictionaries = {}

for i in words:
    for j in i:
        if j not in dictionaries:
            dictionaries[j] = 0
        dictionaries[j] += 1

for i in dictionaries:
    print(f"{i} -> {dictionaries[i]}")