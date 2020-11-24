dictionary = {}


def get(plant, rarity):
    if plant in dictionary:
        dictionary[plant] = [plant, int(rarity), [0, 0]]
    elif plant not in dictionary:
        dictionary[plant] = [plant, int(rarity), [0, 0]]


def rate(plant, rating):
    if plant in dictionary:
        value = dictionary[plant]
        list = value[2]
        list[0] += int(rating)
        list[1] += 1
        dictionary[plant] = [value[0], value[1], list]
    else:
        print("error")


def update(plant, rarity):
    if plant in dictionary:
        value = dictionary[plant]
        new_rarity = rarity
        dictionary[plant] = [value[0], new_rarity, value[2]]
    else:
        print("error")


def reset(plant):
    if plant in dictionary:
        value = dictionary[plant]
        dictionary[plant] = [plant, value[1], [0, 0]]
    else:
        print("error")


def solve():
    n = int(input())
    for i in range(n):
        line = input().split("<->")
        get(line[0], line[1])
    command = input()
    while not command == "Exhibition":
        token = command.split(": ")
        if token[0] == "Rate":
            something = token[1].split(" - ")
            rate(something[0], something[1])
        elif token[0] == "Update":
            something = token[1].split(" - ")
            update(something[0], something[1])
        elif token[0] == "Reset":
            reset(token[1])
        command = input()
    new_dict = {}
    for i in dictionary:
        value = dictionary[i]
        list = value[2]
        if list[1] == 0:
            new_dict[i] = [i, value[1], 0]
        else:
            avr = int(list[0]) / int(list[1])
            new_dict[i] = [i, value[1], avr]
    new_dict2 = sorted(new_dict.values(), key=lambda x: (-int(x[1]), -float(x[2])))
    print("Plants for the exhibition:")
    for i in new_dict2:
        print(f"- {i[0]}; Rarity: {i[1]}; Rating: {i[2]:.2f}")

solve()
