dictionary = {}


def add(piece, composer, key):
    if piece in dictionary:
        print(f"{piece} is already in the collection!")
    elif piece not in dictionary:
        dictionary[piece] = [piece, [composer], key]
        print(f"{piece} by {composer} in {key} added to the collection!")


def remove(piece):
    if piece in dictionary:
        dictionary.pop(piece)
        print(f"Successfully removed {piece}!")
    elif piece not in dictionary:
        print(f"Invalid operation! {piece} does not exist in the collection.")


def change_key(piece, new_key):
    if piece in dictionary:
        value = dictionary[piece]
        dictionary[piece] = [value[0], value[1], new_key]
        print(f"Changed the key of {piece} to {new_key}!")
    elif piece not in dictionary:
        print(f"Invalid operation! {piece} does not exist in the collection.")


def solve():
    p = int(input())
    for i in range(p):
        command = input().split("|")
        dictionary[command[0]] = [command[0], [command[1]], command[2]]
    command = input()
    while not command == "Stop":
        token = command.split("|")
        if token[0] == "Add":
            add(token[1], token[2], token[3])
        elif token[0] == "Remove":
            remove(token[1])
        elif token[0] == "ChangeKey":
            change_key(token[1], token[2])
        command = input()
    new_dict = sorted(dictionary.values(), key=lambda x: (x[0], x[1]))
    for i in new_dict:
        print(f"{i[0]} -> Composer: {', '.join([x for x in i[1]])}, Key: {i[2]}")


solve()
