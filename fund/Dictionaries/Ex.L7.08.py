dictionary = {}

adding = input()

while adding != "End":
    keys = adding.split(" -> ")
    key = keys[0]
    value = keys[1]
    if key not in dictionary:
        dictionary[key] = []
    if value in dictionary[key]:
        pass
    else:
        dictionary[key].append(value)
    adding = input()

dictionary = sorted(dictionary.items(), key=lambda x: x[0])

for key, values in dictionary:
    print(f"{key}")
    for value in values:
        print(f"-- {value}")
