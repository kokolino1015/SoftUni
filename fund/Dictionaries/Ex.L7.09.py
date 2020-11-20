dictionary = {}


def split1(side, name):
    all_users = [item for current_item in dictionary.values() for item in current_item]
    if side not in dictionary:
        dictionary[side] = []
    if name not in all_users:
        dictionary[side].append(name)
        return f"{name} joins the {side} side!"


def split2(name, side):
    if side not in dictionary:
        dictionary[side] = []
    keys = ""
    for key in dictionary:
        for value in dictionary[key]:
            if name in value:
                keys = key
                break
    if keys != "":
        dictionary[keys].remove(name)
        if side not in dictionary:
            dictionary[side] = []

        dictionary[side].append(name)
    else:
        if side not in dictionary:
            dictionary[side] = []

        dictionary[side].append(name)
    return f"{name} joins the {side} side!"


line = input()
while line != "Lumpawaroo":
    if " | " in line:
        token = line.split(" | ")
        side = token[0]
        name = token[1]
        split1(side, name)
    elif " -> " in line:
        token = line.split(" -> ")
        side = token[1]
        name = token[0]
        print(split2(name, side))
    line = input()

dictionary = dict(sorted(dictionary.items(), key=lambda x: ((-len(x[1])), x[0])))

for key, value in dictionary.items():
    if len(value) == 0:
        continue
    print(f"Side: {key}, Members: {len(value)}")
    for i in sorted(value):
        print(f"! {i}")