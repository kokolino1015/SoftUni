collection = input().split(" ")
dictionary = {}

for i in collection:
    word = i.lower()
    if word not in dictionary:
        dictionary[word] = 0
    dictionary[word] += 1

for word in dictionary:
    if dictionary[word] % 2 != 0:
        print(f"{word}", end=" ")
