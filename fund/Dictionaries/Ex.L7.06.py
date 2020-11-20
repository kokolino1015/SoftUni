dictionary = {}

adding = input()

while adding != "end":
    keys = adding.split(" : ")
    key = keys[0]
    value = keys[1]
    if key not in dictionary:
        dictionary[key] = []
    dictionary[key].append(value)
    adding = input()

dictionary = sorted(dictionary.items(), key=lambda x: -len(x[1]))

for key, value in dictionary:
    print(f"{key}: {len(value)}")
    for j in sorted(value):
        print(f"-- {j}")
