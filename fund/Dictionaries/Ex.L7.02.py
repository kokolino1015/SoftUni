dictionary = {}

while True:
    key = input()
    if key == "stop":
        break
    value = int(input())
    if key not in dictionary:
        dictionary[key] = 0
    dictionary[key] += value

for i in dictionary:
    print(f"{i} -> {dictionary[i]}")